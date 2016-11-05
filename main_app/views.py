from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def index(request):
    name = 'main_app/base.html'
    return render(request, 'main_app/index.html', {'template': name})
