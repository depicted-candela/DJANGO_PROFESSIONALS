from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model

## Terminar vista agregando usuario a la vista

def home_view_page(request):
    return HttpResponse(get_user_model().objects.all())