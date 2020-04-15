from django.shortcuts import render
from django.http import HttpResponse

from .controllers import check_template as controller_check_template

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def check_template(request):

    template_ok, err = controller_check_template.check_template()
    if template_ok:
        return HttpResponse("Template Valid !")
    else:
        return HttpResponse("Template not valid. <br/> Check : <br/>"+err)

