from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,get_user_model, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.timezone import activate
from django import forms
from .models import Project, Comment, Note
from .forms import LoginForm, ProjectForm, CommentForm, RegisterForm, NoteForm
from itertools import *
from operator import attrgetter
import itertools

# Create your views here.

def base(request):
    login_form = LoginForm()
    context = {
        'login_form':login_form,
    }
    return render(request, 'base.html', context)

def index(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    context = {
        'register_form':register_form,
        'login_form':login_form,
    }
    return render(request, 'index.html', context)

def profile(request, username):
    projects = Project.objects.all().order_by('-timestamp')
    notes = Note.objects.all().order_by('-timestamp')
    comments = Comment.objects.all().order_by('-timestamp')
    comment_form = CommentForm()
    project_form = ProjectForm()
    note_form = NoteForm()
    update_note_form = NoteForm() 
    dashboard_list = sorted(
        chain(projects, notes),
        key=attrgetter('timestamp'))
    reverse_dashboard_list = sorted(
        chain(projects, notes),
        key=attrgetter('timestamp'), reverse=True)
#    paginator = Paginator(project_list, 5) # Show 25 contacts per page
#    page = request.GET.get('page')
#    try:
#        projects = paginator.page(page)
#    except PageNotAnInteger:
#        # If page is not an integer, deliver first page.
#        projects = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range (e.g. 9999), deliver last page of results.
#        projects = paginator.page(paginator.num_pages)
    query = request.GET.get('query')
    if query:
        dashboard_list = notes.filter(
           Q(note__icontains=query) | Q(name__icontains=query)
        ).order_by('-timestamp').distinct() or projects.filter(
           Q(name__icontains=query) | Q(content__icontains=query)
        ).order_by('-timestamp').distinct()
    context = {
        'comment_form':comment_form,
        'projects':projects,
        'notes':notes,
        'comments':comments,
        'dashboard_list':dashboard_list,
        'reverse_dashboard_list':reverse_dashboard_list,
        'project_form':project_form,
        'note_form': note_form,
        'update_note_form':update_note_form,
    }
    return render(request, 'profile.html', context)

def detail(request, id):
    projects = Project.objects.all()    
    project = get_object_or_404(Project, id=id)
    context = {
        'project':project, 
        'projects':projects,
    }
    return render(request, 'detail.html', context)

def add_comment_to_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.note = note
            comment.save()
            return redirect('profile', user)
    else:
        comment_form = CommentForm()
    return render(request, 'profile.html', {'comment_form':comment_form})

def post_project(request, username):
    project_form = ProjectForm(request.POST, request.FILES or None)
    if project_form.is_valid():
        project = project_form.save(commit=False)
        project.user = request.user
        project.save()
        messages.success(request, 'You have created a new post' )            
        return redirect('profile', username)
    else:
        messages.error(request, 'Not Successfully Created')
    context = {
        'project_form': project_form
    }
    return render(request, 'profile.html', context)

def post_note(request, username):
    note_form = NoteForm(request.POST, request.FILES or None)
    if note_form.is_valid():
        note = note_form.save(commit=False)
        note.user = request.user
        note.save()
        messages.success(request, 'You have created a new note' )            
        return redirect('profile', username)
    else:
        messages.error(request, 'Not Successfully Created')
    context = {
        'note_form': note_form,
    }
    return render(request, 'profile.html', context)

def update_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    instance = get_object_or_404(Note, slug=slug)
    update_note_form = NoteForm(request.POST or None, instance=instance)
    if update_note_form.is_valid():
        instance = update_note_form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'You have updated your Note!')            
        return redirect('profile', instance.user)
    context = {
        'note': note,
        'instance':instance,
        'update_note_form': update_note_form,
    }
    return render(request, 'profile.html', context)

def delete_note(request, slug=None): 
    note = get_object_or_404(Note, slug=slug)
    if request.user == note.user:
        messages.success(request, 'You have deleted your post')
        note.delete()
    return redirect('profile', note.user)

def update_project(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    project_form = ProjectForm(request.POST, request.FILES or None, instance=project)
    if project_form.is_valid():
        instance = project_form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'name':project.name,
        'project':project,
        'project_form': project_form,
    }
    return render(request, 'update_project.html', context)

def delete_project(request, slug=None): 
    project = get_object_or_404(Project, slug=slug)
    if request.user == project.user:
        messages.success(request, 'You have deleted your post')
        project.delete()
    return redirect('profile', project.user)
        
def update_profile(request, username):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('detail')

def like_project(request):
    project_id = request.POST.get('project_id', None)
    likes = 0
    if (project_id):
        project = Project.objects.get(id=int(project_id))
        if project is not None:
            likes = project.likes + 1
            project.likes = likes
            project.save()
    return HttpResponse(likes)

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('profile', user)
            else:
                messages.error(request, 'Incorrect username/password combination')
                return redirect('index')
    else:
        login_form = LoginForm()
        return render(request, 'index.html', {'login_form':login_form})

def logout_view(request, user):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            password = register_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            if new_user is not None and new_user.is_active:
                login(request, new_user)
                messages.success(request, "You've created a new profile")
                return redirect('profile', new_user)
            else:
                messages.error(request, 'Something went wrong with your registration')
                return redirect('base')
    else:
        register_form = RegisterForm()
    return render(request, 'base.html', {'register_form':register_form})