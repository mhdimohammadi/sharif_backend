from django.db import models
from django.templatetags.static import static





class Team(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name= "نام",
    )

    speciality = models.CharField(
        max_length=100,
        verbose_name= "تخصص",
    )

    profile_picture = models.ImageField(
        upload_to="team/profile_pictures",
        null=True,
        blank=True,
        verbose_name= "عکس پروفایل",
    )

    priority = models.PositiveIntegerField(
        default=0,
        verbose_name= "اولویت نمایش",
        help_text= "نشان دهنده الویت نمایش اعضای تیم، عدد بالاتر یعنی الویت بیشتر",
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name= "وضعیت عضو",
        help_text= "فعال یا غیر فعال"
    )


    class Meta:
        verbose_name = "تیم"
        verbose_name_plural = "اعضای تیم"

        indexes = [
            models.Index(
                fields=[
                    'priority',
                ],
            )
        ]


    def __str__(self):
        return f"{self.name} : {self.speciality}"



    # =============================
    # returns default image is there is no profile picture
    # =============================
    @property
    def default_image_fallback(self):
         if self.profile_picture:
             return self.profile_picture.url

         return  static('images/default_pfp.jpg')

