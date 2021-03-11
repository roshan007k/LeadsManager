from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')