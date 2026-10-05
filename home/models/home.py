from django.db import models





class Home(models.Model):

    main_title = models.CharField(
        max_length=100,
        verbose_name="تایتل اصلی"
    )

    short_description = models.TextField(
        max_length=500,
        verbose_name="توضیح کوتاه",
    )

    footer_description = models.TextField(
        verbose_name= "توضیحات فوتر",
        null=True,
        blank=True,
        default= "رایمند شریف"
    )

    banner = models.ImageField(
        upload_to="home/banners",
        verbose_name= "بنر سایت",
    )

    card1_title = models.CharField(
        max_length=100,
        verbose_name= "تایتل کارت اول",
    )

    card1_description = models.TextField(
        max_length=500,
        verbose_name= "توضیح کارت اول",
    )

    card2_title = models.CharField(
        max_length=100,
        verbose_name= "تایتل کارت دوم",
    )

    card2_description = models.TextField(
        max_length=500,
        verbose_name= "توضیح کارت دوم",
    )

    card3_title = models.CharField(
        max_length=100,
        verbose_name= "تایتل کارت سوم",
    )

    card3_description = models.TextField(
        max_length=500,
        verbose_name= "توضیح کارت سوم",
    )

    company_phone = models.CharField(
        max_length=11,
        verbose_name= "شماره تلفن شرکت",
    )

    company_email = models.EmailField(
        max_length=100,
        verbose_name= "ایمیل شرکت",
    )


    site_is_active = models.BooleanField(
        default=True,
        verbose_name= 'فعالی/غیر فعالی سایت'
    )


    class Meta:
        verbose_name = "صفحه اصلی"
        verbose_name_plural = "تنظیمات صفحه اصلی"


    def __str__(self):
        return self.main_title
