from django import forms
from . import models

class OpinionForm(forms.ModelForm):
    class Meta:
        model = models.Opinion
        fields = "__all__"