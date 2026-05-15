from django import forms
from .models import Respondent, Choice


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop("question")
        super().__init__(*args, **kwargs)

        if question.question_type == "MC":
            self.fields["answer"] = forms.ModelChoiceField(
                queryset=Choice.objects.filter(question=question),
                widget=forms.Select
            )
        else:
            self.fields["answer"] = forms.CharField(
                widget=forms.TextInput()
            )


class PersonalInfoForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Respondent
        fields = "__all__"