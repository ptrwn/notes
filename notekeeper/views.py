from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Note, Category
from .forms import NoteForm, CategoryForm


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('notekeeper:index')
    context = {"form": form, }
    template = loader.get_template('registration/signup.html')
    return HttpResponse(template.render(context, request))


def index(request):
    if not request.user.is_authenticated:
        return redirect_to_login(reverse('notekeeper:index'), redirect_field_name='next')
    own_note_list = Note.objects.filter(created_by=request.user)
    template = loader.get_template('notekeeper/index.html')
    context = {
        "latest_note_list": own_note_list
    }
    return HttpResponse(template.render(context, request))


def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if not request.user.id == note.created_by.id:
        return redirect_to_login(reverse('notekeeper:update_note', kwargs={'note_id': note_id}), redirect_field_name = 'next')
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            updated_note = Note.objects.get(id=note_id)
            updated_note.header = form.cleaned_data['header']
            updated_note.body = form.cleaned_data['body']
            updated_note.is_favorite = form.cleaned_data['is_favorite']
            updated_note.category = form.cleaned_data['category']
            updated_note.save()
            return redirect('notekeeper:note_details', note_id=updated_note.id)

    form = NoteForm(initial={
        'header': note.header,
        'body': note.body,
        'is_favorite': note.is_favorite,
        'category': note.category
    })

    context = {
        "form": form,
        "note": note
    }
    template = loader.get_template('notekeeper/update_note.html')
    return HttpResponse(template.render(context, request))


def add_cat(request):
    if not request.user.is_authenticated:
        return redirect_to_login(reverse('notekeeper:index'), redirect_field_name='next')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_cat = Category.objects.create(name=form.cleaned_data['name'])
            new_cat.save()
            return redirect('notekeeper:index')
        else:
            print(form.errors)

    else:
        form = CategoryForm()

    context = {
        "form": form
    }
    template = loader.get_template('notekeeper/newcat.html')
    return HttpResponse(template.render(context, request))


def delete_note(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = Note.objects.get(id=int(note_id))
        if not request.user.id == note.created_by.id:
            return HttpResponse('Forbidden', status=403)
        note.delete()
        return redirect('notekeeper:index')
    return redirect('notekeeper:index')


def note_details(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if not request.user.id == note.created_by.id:
        return redirect_to_login(reverse('notekeeper:note_details', kwargs={'note_id': note_id}), redirect_field_name = 'next')
    context = {
        "note": note
    }
    template = loader.get_template('notekeeper/read.html')
    return HttpResponse(template.render(context, request))


def create_note(request):
    if not request.user.is_authenticated:
        return redirect_to_login(reverse('notekeeper:create_note'), redirect_field_name='next')
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = Note.objects.create(
                header=form.cleaned_data['header'],
                body=form.cleaned_data['body'],
                is_favorite=form.cleaned_data['is_favorite'],
                category=form.cleaned_data['category'],
                created_by=request.user
            )
            return redirect('notekeeper:note_details', note_id=new_note.id)

    form = NoteForm()
    context = {
        "form": form
    }
    template = loader.get_template('notekeeper/newnote.html')
    return HttpResponse(template.render(context, request))


def view_published_note(request, note_uuid):
    note = get_object_or_404(Note, uuid=note_uuid)
    context = {
        "note": note,
    }
    template = loader.get_template('notekeeper/view_published.html')
    return HttpResponse(template.render(context, request))


def publish_note(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = Note.objects.get(id=int(note_id))
        if not request.user.id == note.created_by.id:
            return HttpResponse('Forbidden', status=403)
        note.add_uuid()
        return redirect('notekeeper:view_published', note_uuid=note.uuid)
    return redirect('notekeeper:index')


def unpublish_note(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = Note.objects.get(id=int(note_id))
        if not request.user.id == note.created_by.id:
            return HttpResponse('Forbidden', status=403)
        note.del_uuid()
        return redirect('notekeeper:note_details', note_id=note.id)
    return redirect('notekeeper:index')
