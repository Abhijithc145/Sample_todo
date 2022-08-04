from pyexpat import model
from attr import field
from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task',]