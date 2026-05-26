from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonalInfoForm, AnswerForm
from .models import Respondent, Question

def post_detail(request, pk):
    obj = get_object_or_404(Respondent, pk=pk)
    questions = Question.objects.all()
    forms = []

    for question in questions:
        forms.append({
            "question": question,
            "form": AnswerForm(question=question)
        })
    
    return render(request, "survey.html", {
        "obj": obj,
        "forms": forms
    })

def poll(request):
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return redirect("poll_detail", pk=obj.pk)
    else:
        form = PersonalInfoForm()

    return render(request, "homepage.html", {"form": form})