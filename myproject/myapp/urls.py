from django.urls import path
import myapp.views as views

urlpatterns = [
    path("", views.main_page, name="main_page"),
]