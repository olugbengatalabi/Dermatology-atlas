from accounts.models import Profile
from typing import Type
from diseases.models import DiseaseImage
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def signup_view(request):
  if request.user.is_authenticated:
    return(redirect("index"))
  else:
    if request.method == "POST":
      first_name = request.POST["first_name"]
      last_name = request.POST["last_name"]
      email= request.POST["email"]
      password_1= request.POST["password1"]
      password_2= request.POST["password2"]
      username = request.POST["username"]
      if first_name or last_name != "" and first_name or last_name != None:

        if User.objects.filter(email = email).exists():
          messages.error(request, "An account has already been created using this email ")
          return redirect("signup")
        elif User.objects.filter(username = username).exists():
          messages.error(request, "Username already exists")
          return redirect("signup")
        elif " " in username:
          messages.error(request, "username cannot contain spaces, you can use an underscore '_' instead")
          return redirect("signup")
        elif password_1 != password_2:
          messages.info(request, "passwords are not identical")
          return redirect("signup")
        elif len(password_1) < 8:
          messages.info(request, "password must be atleast 8 characters")
          return redirect("signup")
        else:
          user = User.objects.create_user(email = email, password = password_1, first_name = first_name, last_name= last_name, username = username)
          user.save()
          auth_token = str(uuid.uuid4())
          user.profile.auth_token = auth_token
          user.save()
          print(user.profile.auth_token)
          verification_mail_sender(email, auth_token)
          messages.success(request, "You're now registered, check your email to verify your account")
          return redirect("token_sent")


      else:
        messages.error(request, "Name field(s) cannot be empty")
        return redirect("signup")

  return render(request, "account/signup.html")


def token_sent(request):
  return render(request, "account/token_sent.html")


def verification_mail_sender(email, auth_token):
  subject = "Account Verification"
  message = f'Hi click on the link to verify your account http://127.0.0.1:8000/account/verify/{auth_token}'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [email]
  send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
  profile_obj = get_object_or_404(Profile, auth_token = auth_token)
  if profile_obj:
    if profile_obj.is_verified:
      messages.error(request, "Acount is already verified, no need to re-verify")
    else:
      profile_obj.is_verified = True
      profile_obj.save()
      messages.success(request, "Your account has been verified")
    return redirect(("login"))
  else:
    return redirect("verification_error")

def verification_error(request):
  # if there is a verification error, add an option to send the verification message again
  return render(request, "verification_error.html")

def success(request):
  return render(request, "success.html")


# def login_view(request):
#   if request.user.is_authenticated:
#     return(redirect("index"))
#   else:
#     if request.method == "POST":
#       username = request.POST["username"]
#       password = request.POST["password"]
#       user = auth.authenticate(request, username=username, password=password)
#       if user is not None:
#           # that means the username and password is fouvnd in the database
#           auth.login(request, user)
#           messages.success(request, "you're now logged in")
#           return redirect("index")
#           # make it redirect to the dashboard instead after creating your dashboard page.
#       else:
#         print("user not found")
#         messages.error(request, "Invalid credentials")
#         return redirect("login")

#     else:
#       return render(request, "account/login.html", )
# ? the above is up for removal a
def login_view(request):
  if request.user.is_authenticated:
    return(redirect("index"))
  else:
    if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = auth.authenticate(request, username=username, password=password)
      if user is None :
        messages.error(request, "OOps! Invalid credentials")
        return redirect("login")
      elif not user.profile.is_verified:
        messages.error(request, "You have to verify your account before you can login. check your email for the verification message")
        return redirect("login")

      else:
          auth.login(request, user)
          messages.success(request, "you're now logged in")
          return redirect("index")
    else:
      return render(request, "account/login.html", )


@login_required(login_url="login")
def dashboard_view(request):
  user = request.user
  DiseaseImageList = user.diseaseimage_set.all()
  length = DiseaseImageList.count()
  context = {
    "image_list" : DiseaseImageList,
    "length" : length
  }
  return render(request, "account/dashboard.html",context)



def logout_view(request):
  if request.method == "POST":
    auth.logout(request)
    messages.success(request, "you've been successfully logged out, feel free to login again" )
  return redirect("login")

