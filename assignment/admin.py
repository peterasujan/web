from django.contrib import admin
from assignment.models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.register(Assignment, AssignmentAdmin)
