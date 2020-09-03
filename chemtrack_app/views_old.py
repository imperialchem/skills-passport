from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from . import models
from django.template import loader

from .controllers import check_template as controller_check_template



def index(request):
    template = 'base.html'
    context = {}
    return render(request, template, context)


login_required()
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

login_required()
def check_template(request):

    template_ok, err = controller_check_template.check_template()
    if template_ok:
        return HttpResponse("Template Valid !")
    else:
        return HttpResponse("Template not valid. <br/> Check : <br/>"+err)

