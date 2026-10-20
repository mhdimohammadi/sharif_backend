from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter

from ticket.models import TicketModel


@admin.register(TicketModel)
class TicketModelAdmin(admin.ModelAdmin):
    list_display = ['author','status']
    search_fields = ['author']
    list_filter = [
        'status',
        ('created_at', JDateFieldListFilter),
    ]

    list_editable = ['status']