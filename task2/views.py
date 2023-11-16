import logging

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from .forms import EditProfileForm

logger = logging.getLogger(__name__)


class HomeView(View):
    template_name = "task1/home.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.method == "GET":
            logger.info("not authenticated --->>> returned to login")
            return redirect("login")
        return render(request, self.template_name)


class ProfileView(View):
    template_name = "task2/profile.html"
    form_class = EditProfileForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            logger.info("not authenticated --->>> returned to login")
            return redirect("login")
        form = EditProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = EditProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect("home")
        return render(request, self.template_name, {"form": form})
