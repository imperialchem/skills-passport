from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers
from ..models import Record_descriptor
from django import forms
from django.http import JsonResponse


class update_level_form(forms.Form):
    new_level = forms.IntegerField(required=True)
    descriptor = forms.CharField(required = True)
    state = forms.IntegerField(required=True)


class update_statement_form(forms.Form):
    new_text = forms.CharField()
    descriptor = forms.IntegerField(required = True)
    state = forms.IntegerField(required=True)

def check_level_values(new_level, state):
    if state == 0 or state == 2:
        if new_level >= 1 or new_level <= 6:
            return True
    elif state == 1:
        if new_level >= 1 or new_level <= 3:
            return True
    return False


def check_text_values(new_text, state):
    """
        Overkill function
        There in case in the future checks want to be made on the content of the statements
    """
    if state == 0 or state == 2:
        return True
    elif state == 1:
        return True
    return False

login_required()
def update_statement(request):
    if request.method == 'POST':
        form = update_statement_form(request.POST)
        if form.is_valid():
            print("here")
            descriptor_id = form.cleaned_data["descriptor"]
            new_text = form.cleaned_data["new_text"]
            state = form.cleaned_data["state"]
            print(state)
            descriptor = Record_descriptor.objects.filter(pk=descriptor_id)

            if len(descriptor) == 1 and check_text_values(new_text, state):
                can_modif = controllers.can_modify(descriptor[0].category.record, request.user, state)
                if can_modif:
                    if state == 0:
                       descriptor[0].draft_statement = new_text
                    elif state == 1:
                       descriptor[0].draft_statement = new_text
                    else:
                       descriptor[0].draft_statement = new_text
                    descriptor[0].save()

                    return JsonResponse({"error":False,"success":True})


    return JsonResponse({"error":"Bad query","success":False})


login_required()
def update_level(request):

    if request.method == 'POST':
        form = update_level_form(request.POST)
        if form.is_valid():
            descriptor_id = form.cleaned_data["descriptor"]
            new_level = form.cleaned_data["new_level"]
            state = form.cleaned_data["state"]

            descriptor = Record_descriptor.objects.filter(pk=descriptor_id)

            if len(descriptor) == 1 and check_level_values(new_level, state):
                can_modif = controllers.can_modify(descriptor[0].category.record, request.user, state)
                if can_modif:
                    if state == 0:
                       descriptor[0].draft_level = new_level
                    elif state == 1:
                       descriptor[0].feedback_level = new_level
                    else:
                       descriptor[0].final_level = new_level
                    descriptor[0].save()

                    return JsonResponse({"error":False,"success":True})


    return JsonResponse({"error":"Bad query","success":False})