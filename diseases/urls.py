from django.urls.conf import path

from django.urls import path
from . import views


urlpatterns = [
  path("index", views.index, name = "index"),
  path("<int:id>", views.single_disease, name="single"),
  path("contribution/<int:disease_id>/", views.contribution, name="contribution"),
  path("contribution/", views.contribution, name="contribution")
]
