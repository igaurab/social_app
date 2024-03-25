from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  dob = models.DateField()
  profile_picture = models.ImageField(upload_to=user_directory_path)
