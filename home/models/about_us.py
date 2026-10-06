from django.db import models


class AboutUs(models.Model):

    goal = models.TextField(
        verbose_name= "اهداف شرکت",
    )

    pros1_title = models.CharField(
        max_length=100,
        verbose_name= "ویژگی اول",
    )

    pros1_description = models.TextField(
        max_length=300,
        verbose_name= "توضیح ویژگی اول",
    )

    pros2_title = models.CharField(
        max_length=100,
        verbose_name= "ویژگی دوم",
    )

    pros2_description = models.TextField(
        max_length=300,
        verbose_name= "توضیح ویژگی دوم",
    )

    pros3_title = models.CharField(
        max_length=100,
        verbose_name= "ویژگی سوم",
    )

    pros3_description = models.TextField(
        max_length=300,
        verbose_name= "توضیح ویژگی سوم",
    )

    pros4_title = models.CharField(
        max_length=100,
        verbose_name= "ویژگی چهارم",
    )

    pros4_description = models.TextField(
        max_length=300,
        verbose_name= "توضیح ویژگی چهارم",
    )



    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"


    def __str__(self):
        return f"درباره ما : {self.pk}"
