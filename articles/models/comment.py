from django.db import models

from articles.models import ArticleModel

from django_jalali.db import models as jmodels


class Comment(models.Model):

    article = models.ForeignKey(
        ArticleModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name= "مقاله",

    )


    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name="پاسخ به کامنت",
    )

    author = models.CharField(
        max_length=100,
        verbose_name="نویسنده",
    )

    text = models.TextField(
        verbose_name="متن کامنت"
    )

    created_at = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )

    updated_at = jmodels.jDateTimeField(
        auto_now=True,
        verbose_name="تاریخ به روزرسانی",
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name="فعالی/غیر فعالی"
    )



    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"
        ordering = ['-created_at']


    def __str__(self):
        return self.author
