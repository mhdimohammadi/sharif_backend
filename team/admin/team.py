from django.contrib import admin
from team.models import TeamModel




@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['name','speciality','priority','is_active']
    list_editable = ['speciality','priority','is_active']
    search_fields = ['name']
    list_filter = ['is_active']



