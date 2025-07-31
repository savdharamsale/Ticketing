from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from .forms import UserRegistrationForm


class AuthView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )

        return context


class UserLoginView(LoginView):
    template_name = "auth_login_basic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return TemplateLayout.init(self, context)


class UserRegisterView(FormView):
    template_name = "auth_register_basic.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("auth-login-basic")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return TemplateLayout.init(self, context)
