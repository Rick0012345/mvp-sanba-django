from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(redirect_field_name="account_login"), name="dispatch")
class MainPage(TemplateView):
    template_name = "main.html"
