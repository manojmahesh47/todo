from . models import Task
from django import forms

class todo_form(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']


