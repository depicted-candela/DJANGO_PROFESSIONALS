from django.urls import path
from .views import home_view_page, SignUpPageView

urlpatterns = [
    path("", home_view_page, name="home"),
    path("signup/", SignUpPageView.as_view(), name="signup"), # This needs tests
]