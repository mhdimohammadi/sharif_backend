from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
        default="",
    )

    year  = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100),
        ],
        verbose_name= "سال تایم لاین",
        default=1900,
    )
