from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


def index(request):
  if request.user.is_anonymous:
    return redirect('login')
  return redirect('homepage')

def logout_user(request):
  logout(request)
  return redirect('index')

class LoginPage(View):
  template_name = 'accounts/login.html'
  def get(self, request):
    return render(request,"accounts/login.html")
  
  def post(self, request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('homepage')
    
    errors = dict(form.errors.items())
    errors['all'] = errors.pop('__all__', None)
    
    return render(request, self.template_name, {'form_error': errors})
  
class RegisterPage(View):
  template_name = 'accounts/register.html'
  def get(self, request):
    return render(request,"accounts/register.html")
  
  def post(self, request):
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    
    errors = dict(form.errors.items())
    errors['all'] = errors.pop('__all__', None)
    
    return render(request, self.template_name, {'form_error': errors})
