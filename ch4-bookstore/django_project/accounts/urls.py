from django.urls import path
from .views import home_view_page

urlpatterns = [
    path("", home_view_page, name="home")
]