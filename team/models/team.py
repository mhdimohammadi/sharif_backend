from django.db import models






class Team(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name= "نام",
    )

    speciality = models.CharField(
        max_length=100,
        verbose_name= "تخصص",
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name= "وضعیت عضو",
        help_text= "فعال یا غیر فعال"
    )


    class Meta:
        verbose_name = "تیم"
        verbose_name_plural = "اعضای تیم"


    def __str__(self):
        return f"{self.name} : {self.speciality}"