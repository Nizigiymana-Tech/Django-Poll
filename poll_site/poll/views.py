from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PersonalInfoForm, AnswerForm
from .models import Respondent, Question, Answer

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
        respondent_id = request.POST.get("pollData")

        if respondent_id:
            respondent = get_object_or_404(Respondent, pk=respondent_id)
            for question in Question.objects.all():
                answer = request.POST.get(f"question_{question.id}")
                if question.question_type == "MC":
                    Answer.objects.create(
                        respondent=respondent,
                        question=question,
                        choice_id=answer
                    )

                else:
                    Answer.objects.create(
                        respondent=respondent,
                        question=question,
                        text_answers=answer
                    )

            return HttpResponse("Finished")
        else:
            form = PersonalInfoForm(request.POST)

            if form.is_valid():
                obj = form.save()
                return redirect("poll_detail", pk=obj.pk)

    else:
        form = PersonalInfoForm()

    return render(request, "homepage.html", {"form": form})