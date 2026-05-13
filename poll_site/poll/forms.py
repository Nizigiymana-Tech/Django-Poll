from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    
    class Meta:
        model = PersonalInfo
        fields = "__all__"