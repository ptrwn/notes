from django.shortcuts import render
from django.http import HttpResponse
from.models import Note


def index(request):
    latest_note_list = Note.objects.order_by('-created_on')[:5]
    output = ', '.join([n.header for n in latest_note_list])
    return HttpResponse(output)

def note_details(request, note_id):
    return HttpResponse("You're looking at note %s." % note_id)

