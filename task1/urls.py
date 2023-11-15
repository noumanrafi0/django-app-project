from django.urls import path

from .views import EditView, HomeView, LoginView, LogoutView, SignupView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("edit/", EditView.as_view(), name="edit"),
]
