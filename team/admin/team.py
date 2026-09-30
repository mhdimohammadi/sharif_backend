from django.contrib import admin
from team.models import TeamModel




@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['name','speciality']
    list_editable = ['speciality']
    search_fields = ['name']
    list_filter = ['is_active']



