# -*- encoding: utf-8 -*-
from django import forms
from distribution.models import Event

class TestForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Не выбранно", label="События")