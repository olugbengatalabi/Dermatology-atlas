from django.contrib import admin
from .models import *
# Register your models here.
class DiseaseAdmin(admin.ModelAdmin):
  list_display = ["thumbnail", "name", "view_count", "featured", "created"]
  list_display_links = ["thumbnail"]
  list_editable = [ "featured"]
  list_filter = ["featured", "view_count"]

class DiseaseImageAdmin(admin.ModelAdmin):
  list_display = ["disease", "user", "upload_date","verified", "featured"]
  list_editable = ["featured", "verified"]
  list_filter = ["featured", "verified"]

class ThumbnailAdmin(admin.ModelAdmin):
  list_display = ["diseaseName","image","upload_date", "featured", "user"]

  list_editable = ["featured"]
  list_filter = ["upload_date"]


admin.site.register(Disease, DiseaseAdmin)
admin.site.register(DiseaseImage, DiseaseImageAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)

