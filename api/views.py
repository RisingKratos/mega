from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_api_view(request, email, password):
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"value" : "true"})
    return JsonResponse({"value" : "false"})
