from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Feature(models.Model):

    title = models.CharField(
        max_length=50,
        verbose_name='تایتل ویژگی',
    )

    description = models.TextField(
        max_length=150,
        verbose_name='توضیح ویژگی',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name= "فعلی/غیر فعالی",
    )

    priority = models.IntegerField(
        default=0,
        verbose_name= "الویت نمایش",
    )

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

        ordering = ['-priority']

        indexes = [
            models.Index(
                fields=['priority'],
            )
        ]


    def __str__(self):
        return f"{self.title} : {self.description}"




class TimeLine(models.Model):

    title = models.CharField(
        max_length=50,
        verbose_name= "تایتل تایم لاین",
        default="",
    )

    description = models.CharField(
        max_length=100,
        verbose_name= "توضیح تایم لاین",
        default="",
    )

    bridge_text = models.CharField(
        max_length=100,
        verbose_name= "توضیح پل",
        help_text= "متنی که بین دو بخش مختلف تایم لاین روی خط نمایش داده میشود",
        null=True,
        blank=True,
    )

    year  = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(9999),
        ],
        verbose_name= "سال تایم لاین",
        default=1900,
        unique=True,
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name= "فعالی/غیر فعالی",
    )


    class Meta:

        verbose_name = "خط زمانی"
        verbose_name_plural = "خط های زمانی"

        ordering = ['year']

        indexes = [
            models.Index(
                fields=['year'],
            )
        ]



    def __str__(self):
        return f"{self.title} : {self.bridge_text}"



    def clean(self):
        super().clean()

        max_year = (
            TimeLine.objects
            .exclude(pk=self.pk)
            .aggregate(max_year=models.Max("year"))
            ["max_year"]
        )

        if max_year is not None and self.year >= max_year and self.bridge_text:
            raise ValidationError({
                "bridge_text": "برای جدیدترین خط زمانی، توضیح پل نباید وارد شود."
            })