import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View

from .forms import EditProfileForm
from .models import Profile

logger = logging.getLogger(__name__)


class HomeView(LoginRequiredMixin, View):
    template_name = "task1/home.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        user_data = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_data)
        return render(
            request,
            self.template_name,
            {"user_data": user_data, "user_profile": user_profile},
        )


class ProfileView(View):
    template_name = "task2/profile.html"
    form_class = EditProfileForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            logger.info("not authenticated --->>> returned to login")
            return redirect("login")

        try:
            profile = request.user.profile
            form = EditProfileForm(instance=profile)
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=request.user)
            form = EditProfileForm(instance=profile)

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
