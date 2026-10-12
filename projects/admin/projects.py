from django.contrib import admin
from projects.models import ProjectModel,ProjectImagesModel
from django_jalali.admin.filters import JDateFieldListFilter


class ProjectImagesModelInline(admin.TabularInline):
    model = ProjectImagesModel
    extra = 1
    show_change_link = True




@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):

    inlines = [ProjectImagesModelInline]

    list_display = (
        'name',
        'start_date',
        'end_date',
    )

    search_fields = (
        'title',
        'description'
    )

    list_filter = [
        'is_active',
        ('start_date', JDateFieldListFilter),
        ('end_date', JDateFieldListFilter),
    ]
