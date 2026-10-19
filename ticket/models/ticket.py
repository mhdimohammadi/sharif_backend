from django.db import models
from django.core.exceptions import ValidationError




class Ticket(models.Model):

    class Status(models.TextChoices):
        OPEN = 'open' , 'باز'
        CLOSED = 'closed' , 'بسته'
        ANSWERED = 'answered' , 'پاسخ داده شده'

    author = models.CharField(
        max_length=250,
        verbose_name="نام و نام خانوادگی کاربر",
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=11,
        verbose_name="شماره تلفن کاربر",
        null=True,
        blank=True,
    )

    message = models.TextField(
        verbose_name="متن تیکت",
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.OPEN,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name= "تاریخ ایجاد",
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name= "تاریخ به روزرسانی",
        null=True,
        blank=True,
    )


    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"
        ordering = ["-created_at"]

    def __str__(self):
        return self.author

    def clean(self):
        super().clean()

        if not self.phone_number.isdigit():
            raise ValidationError('شماره تلفن باید کاملا عددی باشد')

        if not self.phone_number.startswith('09'):
            raise ValidationError('شماره تلفن باید با 09 آغاز شود')

        if len(self.phone_number) != 11:
            raise ValidationError('شماره تلفن باید 11 رقم باشد')
