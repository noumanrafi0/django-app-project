from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Format: +999999999,  Up to 15 digits max.",
            )
        ],
        null=True,
    )
    address = models.TextField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(
        default="profile_images/default.jpg",
        upload_to="profile_images",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username
