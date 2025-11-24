from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm


def home(request):
    form = ProfileForm()

    return render(request, "student/home.html", {"form": form})
