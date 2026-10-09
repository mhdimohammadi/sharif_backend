from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from django.conf import settings
from django.templatetags.static import static




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

    image = models.ImageField(
        upload_to='articles/',
        verbose_name= "تصویر مقاله",
        null=True,
        blank=True,
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

    priority = models.PositiveIntegerField(
        default=0,
        verbose_name= "الویت نمایش",
        help_text= "هرچه عدد بالاتر باشد الویت نمایش مقاله بیشتر است",
    )

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-priority']

        indexes = [
            models.Index(
                fields=['priority'],
            )
        ]



    def get_absolute_url(self):
        return reverse("articles:article_detail", args=[self.id])


    def __str__(self):
        return f"{self.author}: {self.title}"


    # =============================
    # returns default image is there is no articles picture
    # =============================
    @property
    def default_image_fallback(self):
         if self.image:
             return self.image.url

         return  static('images/default_article.jpg')