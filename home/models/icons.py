from django.db import models
from django.utils.html import format_html


class Icon(models.Model):

    image = models.ImageField(
        upload_to='icons/',
        verbose_name= "لوگو",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعالی غیر فعالی",
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نام مشتری (برای alt)",
        default='',
    )

    priority = models.IntegerField(
        default=0,
        verbose_name="الویت نمایش",
    )


    class Meta:
        verbose_name = "لوگو"
        verbose_name_plural = "لوگو ها"
        ordering = ['-priority','-id']


    def __str__(self):
        return self.title or f"آیکون {self.pk}"

    @property
    def get_icon(self):
        if not self.image:
            return ""
        return format_html('<img src="{}" alt="{}" loading="lazy">',self.image.url,self.title or "logo")
