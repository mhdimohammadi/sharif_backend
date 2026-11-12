from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from django.templatetags.static import static



class Project(models.Model):

    objects = jmodels.jManager()


    name = models.CharField(
        max_length=100,
        verbose_name="نام خبر",
    )

    description = models.TextField(
        verbose_name="توضیحات خبر",
    )

    start_date = jmodels.jDateTimeField(
        verbose_name="تاریخ",
    )


    source = models.CharField(
        max_length=300,
        verbose_name="منبع",
        null=True,
        blank=True,
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name= "فعالی/غیر فعالی",
    )


    cover_image = models.ImageField(
        upload_to='projects/cover_images/',
        null=True,
        blank=True,
        verbose_name= "عکس کاور",
    )

    class Meta:
        verbose_name = "خبر و رویداد"
        verbose_name_plural = "اخبار و رویداد ها"

        ordering = ["-start_date"]

        indexes = [
            models.Index(
                fields=['-start_date'],
            ),
        ]



    def get_absolute_url(self):
        return reverse("projects:project_detail", args=[self.id])


    def __str__(self):
        return self.name


    # =============================
    # returns default image is there is no articles picture
    # =============================
    @property
    def default_image_fallback(self):
         if self.cover_image:
             return self.cover_image.url

         return  static('images/default_project.jpg')





class ProjectImages(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name= "خبر",
    )

    big_image = models.ImageField(
        upload_to='projects/big_images/',
        null=True,
        blank=True,
        verbose_name= "عکس بزرگ خبر",
    )

    small_image1 = models.ImageField(
        upload_to='projects/small_images/',
        null=True,
        blank=True,
        verbose_name= "عکس کوچک اول خبر",
    )

    big_image2 = models.ImageField(
        upload_to='projects/small_images/',
        null=True,
        blank=True,
        verbose_name='عکس کوچک دوم خبر',
    )