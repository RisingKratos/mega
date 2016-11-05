from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main_app.models import AbstractUser
from profile.forms import UploadFileForm
import os

@login_required
def profile_view(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)

            new_first_name = request.POST['firstName']
            new_last_name = request.POST['lastName']
            new_worked_at = request.POST['experience']
            new_phone_number = request.POST['phoneNumber']

            newUser = request.user
            newUser.first_name = new_first_name
            newUser.last_name = new_last_name
            newUser.abstractuser.work = new_worked_at
            newUser.abstractuser.phone = new_phone_number

            if form.is_valid():
                newUser.abstractuser.profile_image = request.FILES['file']
            newUser.save()
            newUser.abstractuser.save()

        else:

            codes = request.user.abstractuser.codes.all()
            return render(request, 'profile/profile.html', {'user' : request.user, 'codes' : codes})

        return redirect('profile')
    else:
        return redirect('auth')

def profile_show(request, profile_id):
    profile = get_object_or_404(User, pk=profile_id)
    return render(request, 'profile/show.html', {'profile': profile})
