from django.urls import path
from . import views
urlpatterns = [
    path("signup", views.signup_view, name="signup"),
    path("dashboard", views.dashboard_view, name ="dashboard"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("verification_error", views.verification_error, name="verification_error"),
    path("verify/<auth_token>", views.verify, name = "verify"),
    path("password_change1", views.password_change1, name="password_change1"),
    path("password_change2/<auth_token>", views.password_change2, name="password_change2")
]
