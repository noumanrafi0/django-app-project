from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomeView, ProfileView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("profile/", ProfileView.as_view(), name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
