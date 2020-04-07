from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("notekeeper index")

def note_details(request, note_id):
    return HttpResponse("You're looking at note %s." % note_id)
