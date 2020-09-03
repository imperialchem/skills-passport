from django.shortcuts import render, redirect

def index(request):
    template = 'base.html'
    context = {}
    return render(request, template, context)
