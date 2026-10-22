from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from django.templatetags.static import static





class Project(models.Model):

    objects = jmodels.jManager()

    class Status(models.TextChoices):
        DONE = 'done' , 'تمام شده',
        ONGOING = 'ongoing','در حال انجام'

    name = models.CharField(
        max_length=100,
        verbose_name="نام پروژه",
    )

    description = models.TextField(
        verbose_name="توضیحات پروژه",
    )

    start_date = jmodels.jDateTimeField(
        verbose_name="تاریخ شروع",
    )

    end_date = jmodels.jDateTimeField(
        verbose_name="تاریخ پایان",
    )

    costumer = models.CharField(
        max_length=100,
    verbose_name="نام و نام خانوادگی مشتری",
    )

    location = models.CharField(
        max_length=50,
        verbose_name="محل پروژه",
    )

    worth = models.CharField(
        max_length=100,
        verbose_name= "ارزش پروژه",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name= "فعالی/غیر فعالی",
    )

    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.ONGOING,
        verbose_name= "وضعیت پروژه",
    )

    cover_image = models.ImageField(
        upload_to='projects/cover_images/',
        null=True,
        blank=True,
        verbose_name= "عکس کاور",
    )

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

        ordering = ["-start_date"]

        indexes = [
            models.Index(
                fields=['-start_date'],
            ),

            models.Index(
                fields=['-end_date']
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
        verbose_name= "پروژه",
    )

    big_image = models.ImageField(
        upload_to='projects/big_images/',
        null=True,
        blank=True,
        verbose_name= "عکس بزرگ پروژه",
    )

    small_image1 = models.ImageField(
        upload_to='projects/small_images/',
        null=True,
        blank=True,
        verbose_name= "عکس کوچک اول پروژه",
    )

    big_image2 = models.ImageField(
        upload_to='projects/small_images/',
        null=True,
        blank=True,
        verbose_name='عکس کوچک دوم پروژه',
    )