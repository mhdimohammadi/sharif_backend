from django.db import models

from articles.models import ArticleModel




class Comment(models.Model):

    article = models.ForeignKey(
        ArticleModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name= "مقاله",

    )

    replies = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
    )

    author = models.CharField(
        max_length=100,
        verbose_name="نویسنده",
    )

    text = models.TextField(
        verbose_name="متن کامنت"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )

    updated_at = models.DateTimeField(
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
