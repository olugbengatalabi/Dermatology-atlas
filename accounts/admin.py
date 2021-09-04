from django.contrib import admin
from . models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = [ "user", "created_at", "is_verified"]
    list_display_links = ["user"]


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
