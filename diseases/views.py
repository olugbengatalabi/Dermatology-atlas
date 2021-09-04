from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.deletion import SET_NULL
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Disease, DiseaseImage
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

# Create your views here.
def index(request):
  queryset = Disease.objects.filter(featured=True)
  if request.method == "GET":
    if "search" in request.GET:
      search= request.GET["search"]
      if search != "" and search is not None:
        queryset = Disease.objects.filter(Q(name__icontains=search) | Q(
            other_name_1__icontains=search) | Q(other_name_2__icontains=search) | Q(other_name_3__icontains=search))
  paginator = Paginator(queryset, 6)
  page = request.GET.get('page')
  paged_diseases = paginator.get_page(page)
  context = {
    "diseases" : paged_diseases,
  }
  return render(request, "diseases/index.html",context)

def single_disease(request, id):
  disease = get_object_or_404(Disease, id=id)
  images =disease.diseaseimage_set.all()
  disease.view_count += 1
  disease.save()
  print(disease.view_count)
  context = {
    "disease":disease,
    "images":images,
  }
  return render(request, "diseases/single-disease.html", context)


@login_required(login_url="login")
def contribution(request, disease_id = 0):
  all_disease = Disease.objects.all()
  try:
    selected_disease = get_object_or_404(Disease, id = disease_id)
  except:
    selected_disease = 0
  if request.method == "POST" and request.FILES["image"]:
        name = request.POST["name"]
        image = request.FILES["image"]
        note = request.POST["note"]
        user = request.user
        disease = get_object_or_404(Disease, name = name)
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        upload_file_url = fs.url(filename)
        DiseaseImage.objects.create(disease = disease, user = user, extra_information = note, image = filename)
        messages.success(request, "Thank you for your contribution, expect an email from us soon")
        send_mail(
          "Dermatology Atlas thanks you for your contribution",
          "Thank you for your contribution, our team will verify the image.",
          [user.email],
          fail_silently=False
        )
        
  if selected_disease:

    context = {
      "selected_disease": selected_disease,
      "diseases": all_disease
    }
  else:
    context = {
      "diseases": all_disease
    }
  return render(request, "diseases/contribution.html", context)
# add a feature that sends you an email anytime someone sends in a contribution