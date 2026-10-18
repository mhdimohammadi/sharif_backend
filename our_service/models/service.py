from django.db import models
from django.utils.html import format_html



class Service(models.Model):

    class IconChoices(models.TextChoices):
        SUN = "sun" , "خورشید"
        GEAR = "gear" , "چرخدنده"
        GEARS = "gears" , "چرخدنده ها"
        PENCIL = "pencil" , "مداد"
        TOWER = "tower" , "برج"
        TOOLS = "tools" , "ابزار"
        CHART = "chart" , "جدول"
        LIKE = "like" , "لایک"


    title = models.CharField(
        max_length=100,
        verbose_name='عنوان',
        default='',
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name= "توضیح",
        help_text= "توضیحی که برای خدمات در صفحه اصلی نمایش داده میشود",
    )

    priority = models.IntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )

    icon = models.CharField(
        max_length=100,
        choices=IconChoices.choices,
        default=IconChoices.SUN,
        verbose_name= "آیکون",

    )

    ICON_CLASSES = {
        IconChoices.SUN: "fa-sun",
        IconChoices.GEAR: "fa-gear",
        IconChoices.GEARS: "fa-gears",
        IconChoices.PENCIL: "fa-pen-to-square",
        IconChoices.TOWER: "fa-building",
        IconChoices.TOOLS: "fa-screwdriver-wrench",
        IconChoices.CHART: "fa-table",
        IconChoices.LIKE: "fa-thumbs-up",
    }

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات ما"
        ordering = ['-priority']



    def __str__(self):
        return self.title


    @property
    def get_icon(self):
        icon_class = self.ICON_CLASSES.get(self.icon, "fa-sun")
        return format_html('<span class="icon-services"><i class="fa-solid {}"></i></span>',icon_class)

