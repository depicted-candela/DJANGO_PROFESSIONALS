from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

# THe home view that renders all the Custon Users
def home_view_page(request):
    return HttpResponse(get_user_model().objects.all())

class SignUpPageView(generic.CreateView):
    """The view for Signin Ups that creates new Custom Users

    Args:
        generic (CreateView): A view for creating objects for models of the database
    """
    form_class      = CustomUserCreationForm    # The form to be rendered in the html accessed
                                                # with template_name when this view is used
    success_url     = reverse_lazy("login")     # When the creation process of a Custom User is successfull
                                                # go to the login url
    template_name   = "registration/signup.html"# The html file to be rendered when the url of this view
                                                # is accessed
    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, any]:
        """Customization of the get_context_data from generic.CreateView to add in the context the form

        Returns:
            dict[str, Any]: the context of the view that renders the form of the view that creates CustomUsers
        """
        context = super().get_context_data(**kwargs)
                                                # Creates a key for the form: useful when many elements are rendered in the view
        context["signup-form"] = self.get_form()
        return context