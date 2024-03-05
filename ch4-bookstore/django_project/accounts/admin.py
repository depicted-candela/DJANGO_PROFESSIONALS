from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Shortcut for importing the custom User Model
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form    = CustomUserCreationForm ## The form for adding new users
    form        = CustomUserChangeForm   ## The form for changing new users
    model       = CustomUser
    list_display = [    ## Showing some characteristics to be editable
        "email",
        "username",
        "is_superuser",
    ]

admin.site.register(CustomUser, CustomUserAdmin)