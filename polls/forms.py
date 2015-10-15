from django import forms
from .models import Question, Choice
from datetime import datetime


class ChoiceForm(forms.ModelForm):
    choice = forms.IntegerField(widget=forms.RadioSelect(), initial=1)

    class Meta:
        model = Choice
        fields = "__all__"
