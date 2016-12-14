from django import forms
from django.contrib.auth.models import User
from .models import Project, Comment,Note

class LoginForm(forms.Form):
    username = forms.CharField(
        label=False, 
        max_length=64, 
        widget=forms.TextInput(attrs={'placeholder': 'username'}))

    password = forms.CharField(
        label=False, 
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    remember_me = forms.BooleanField(
        required=False, label='Remember me')

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        max_length=64, 
        label=False, 
        widget=forms.TextInput(attrs={'placeholder': 'username'}))

    email = forms.EmailField(
        max_length=255, 
        label=False, 
        widget=forms.TextInput(attrs={'class': 'register-label', 'placeholder': 'email'}))

    password = forms.CharField(
        min_length=8, 
        label=False, 
        widget=forms.PasswordInput(attrs={'class':'register-label', 'placeholder': 'password'}))

    agreement = forms.BooleanField(
        required=True, 
        label='I agree to DesignsCub3d terms')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'agreement',
        ]

class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        label='3D Model Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '3D Model Name' }))

    class Meta:
        model = Project
        fields = ['name', 'document']

class NoteForm(forms.ModelForm):
    name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Note title'}))

    note = forms.CharField(
        label=False,
        max_length=200,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Write your note here...'}))

    class Meta:
        model = Note
        fields = ['name', 'note',]
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Comment...'}))

    class Meta:
        model = Comment
        fields = ['comment']