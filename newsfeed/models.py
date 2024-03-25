from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/posts/{instance.post.id}/{filename}'

class Post(models.Model):
  text_content = models.TextField(blank=False, null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(default=timezone.now)
  date_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Post {self.id}: {self.text_content[:20]}...."
  
class PostFileUploads(models.Model):
  POST_TYPE = (
     ("A","Attachments"),
     ("P", "Picture")
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='uploads')
  file_path = models.FileField(upload_to=user_directory_path)
  post_type = models.CharField(max_length=10, choices=POST_TYPE)
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"Upload {self.id} by {self.user.username} on {self.post}"