from django.urls import path
from sanba.views import MainPage

urlpatterns = [
    path("", MainPage.as_view(), name="mainpage"),
]
