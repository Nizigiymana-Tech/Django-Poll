from django import forms
from .models import Voter

class PersonalInfoForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    
    class Meta:
        model = Voter
        fields = "__all__"