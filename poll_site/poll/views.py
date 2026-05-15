from django.shortcuts import render, HttpResponse  # noqa: F401
from .forms import PersonalInfoForm

def poll(request):
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return render(request, "survey.html", {"obj": obj})
    else:
        form = PersonalInfoForm()

    return render(request, "homepage.html", {"form": form})