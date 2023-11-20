import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from .forms import EditForm, LoginForm, SignupForm

logger = logging.getLogger(__name__)


class HomeView(LoginRequiredMixin, View):
    template_name = "task1/home.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SignupView(View):
    template_name = "task1/signup.html"
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("confirm_password")

            if password != confirm_password:
                messages.error(request, "Password does not match")
                return redirect("signup")

            User.objects.create_user(
                username=username,
                password=password,
            )

            return redirect("login")

        messages.error(request, "Invalid form submission")
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    template_name = "task1/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                logger.info(f"{user} logged in")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("login")
        else:
            messages.error(request, "Invalid form submission")
            return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        logout(request)
        logger.info(f"{username} logged out")
        return redirect("login")


class EditView(LoginRequiredMixin, View):
    template_name = "task1/edit.html"
    login_url = "login"
    form_class = EditForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        user_instance = request.user
        form = self.form_class(request.POST, instance=user_instance)

        if form.is_valid():
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("confirm_password")

            if password and password == confirm_password:
                user_instance.set_password(password)
                form.save()
                messages.success(request, "Password updated successfully")
                return redirect("home")
            else:
                messages.error(
                    request,
                    "Invalid Password or Passwords do not match",
                )

        return render(request, self.template_name, {"form": form})
