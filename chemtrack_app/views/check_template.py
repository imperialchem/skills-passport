from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .. import controllers


login_required()
def check_template(request):

    template_ok, err = controllers.check_template()
    if template_ok:
        return HttpResponse("Template Valid !")
    else:
        return HttpResponse("Template not valid. <br/> Check : <br/>"+err)