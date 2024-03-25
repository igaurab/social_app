from django.shortcuts import render
from django.views import View
from .models import Post, PostFileUploads

class HomePage(View):
  template_name = 'newsfeed/home.html'

  def get(self, request):
    all_posts = Post.objects.filter(user=request.user).prefetch_related('uploads')
    return render(request, self.template_name, {"user": request.user, "posts": all_posts})

  def post(self, request):
    pictures = request.FILES.getlist("pictures")
    attachments = request.FILES.getlist("attachments")
    
    text_content = request.POST.get("post_data")
    post = Post.objects.create(
      user=request.user,
      text_content = text_content
    )
    post.save()
    for picture in pictures:
      _ = PostFileUploads.objects.create(
        user=request.user,
        post = post,
        file_path=picture,
        post_type="P"
      )

    for attachment in attachments:
      _ = PostFileUploads.objects.create(
        user=request.user,
        post = post,
        file_path=attachment,
        post_type="A"
      )

    return render(request, self.template_name, {'user': request.user})