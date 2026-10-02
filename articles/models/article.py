from django.db import models
from django_jalali.db import models as jmodels
from django.conf import settings




class Article(models.Model):

    objects = jmodels.jManager()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name= 'articles',
        verbose_name= 'نویسنده',
    )

    title = models.CharField(
        max_length=100,
        verbose_name='عنوان مقاله',
    )

    content = models.TextField(
        verbose_name= 'محتوای  مقاله',
    )


    created_at = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name= "تاریخ ایجاد",
    )

    updated_at = jmodels.jDateTimeField(
        auto_now=True,
        verbose_name= 'تاریخ به روز رسانی ',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name= 'فعال/غیر فعال'
    )

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


        indexes = [
            models.Index(
                fields=['created_at']
            )
        ]