from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# The form to create new AbstractUser, associated with the geared user in settings.py using get_user_model
class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = (
			"email",
			"username",
		)

# The form to change AbstractUser, associated with the geared user in settings.py using get_user_model
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = get_user_model()
		fields = (
			"email",
			"username",
		)
