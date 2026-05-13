from django.shortcuts import render, HttpResponse
from .forms import PersonalInfoForm

def poll(request):
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponse(f"Created Object with Name: {obj.name}")

    else:
        form = PersonalInfoForm()

    return render(request, "homepage.html", {"form": form})