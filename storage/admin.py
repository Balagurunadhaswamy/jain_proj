from django.contrib import admin
from .models import File
# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ['sent_by', 'recieved_by', 'notified']

admin.site.register(File, FileAdmin)