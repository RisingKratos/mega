from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

'try to do one-to-one relation'
class Code(models.Model):
    code_id = models.IntegerField(blank = True, null = True)
    gem_type = models.IntegerField(blank = True, null = True)
    gems = models.IntegerField(blank = True, null = True)

class AbstractUser(models.Model):
    # Connect To Django authorization
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(null = True, blank = True)
    phone = models.CharField(max_length = 20, null = True, blank = True, default = "")
    work = models.CharField(max_length = 100, null = True, blank = True, default = "")
    gender = models.BooleanField(default = True)
    send_email = models.BooleanField(default = True)
    home = models.CharField(max_length = 250, null = True, blank = True, default = "")
    profile_image = models.ImageField(upload_to = 'Images/', blank = True, null = True)
    data_of_birth = models.DateField(null = True, blank = True)
    codes = models.ManyToManyField(Code, blank = True)
    # Django authorization
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            up = AbstractUser(user=user)
            up.save()

    post_save.connect(create_profile, sender=User)
