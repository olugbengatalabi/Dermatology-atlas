from django.urls import path
from . import views
urlpatterns = [
    path("signup", views.signup_view, name="signup"),
    path("dashboard", views.dashboard_view, name ="dashboard"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    # path("token",views.token_sent, name = "token_sent" ),
    # path("success", views.success, name = "success"),
    # path("verification_error", views.verification_error, name="verification_error"),
    # path("verify/<auth_token>", views.verify, name = "verify")
]
