# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from distribution.models import Event
from distribution.forms import TestForm
from django.template import RequestContext

def index(request):

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['event']
            text = Event().anchor(cd.id,1)
            return render_to_response('formtest.html', {'text': text})
    else:
        form = TestForm()
        return render_to_response('formtest.html', {'form': form},context_instance=RequestContext(request))