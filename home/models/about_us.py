from django.db import models



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


class TimeLine(models.Model):
    pass