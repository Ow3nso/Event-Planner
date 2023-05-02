from dataclasses import fields

from django.forms import ImageField, ModelForm, TextInput, EmailInput, IntegerField

from django import forms
from flask import request
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"