from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main_app.models import Code
from django.shortcuts import render, get_object_or_404

# Create your views here.
def login_api_view(request, email, password):
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"value" : "true"})
    return JsonResponse({"value" : "false"})

def gem_api_view(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    if code is not None:
        code.gems -= 1
        code.save()
        return JsonResponse({"value" : "true"})
    return JsonResponse({"value" : "false"})
