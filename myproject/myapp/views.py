from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.

def main_page(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(
        request,
        template_name="index.html",
        context=context
    )