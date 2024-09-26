from django.contrib import admin

# Register your models here.
from .models import NewUser

class NewUserAdmin(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(NewUser, NewUserAdmin)