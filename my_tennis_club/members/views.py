from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .form import FeedbackForm
from .models import Feedback
from django.contrib.admin.views.decorators import staff_member_required



def home(request):
  template = loader.get_template('tem_members/home.html')
  return HttpResponse(template.render())

def myfirst(request):
  template = loader.get_template('tem_members/myfirst.html')
  return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('tem_members/all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('tem_members/details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('tem_members/main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.filter(Q(firstname='Endurance') | Q(firstname='okoi')).values()
  template = loader.get_template('tem_members/template.html')
  context = {
    'mymembers': mydata,

  }
  return HttpResponse(template.render(context, request)) 

def syntax(request):
  template = loader.get_template('tem_members/syntax.html')
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }],
      'greeting': 1,
      'x': ['Apple', 'Banana', 'Cherry'], 
      'y': ['Apple', 'Banana', 'Cherry'], 

    
    }
  return HttpResponse(template.render(context, request)) 


def register_user(request):
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      confirm_password = request.POST.get("confirm_password")
      
      if not username or not password or not confirm_password:
        messages.error(request, "All fields are required .")
        return redirect('members:register')
      
      
      elif  password != confirm_password:
        messages.error(request, "password do not match .")
        return redirect('members:register')

      elif User.objects.filter(username=username).exists():
        messages.error(request, "username already taken  .")
        return redirect('members:register')
      try:
          user = User.objects.create_user(username=username, password=password)
          user.save()
          messages.success(request, "Registration successful!")
          return redirect('members:login')
      except  Exception as e:
          messages.error(request, f"Error: {e}")
          return redirect('members:register')
      
    return render(request, 'registration/register.html')




def login_user(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('members:profile')
    
    else:
      messages.error(request,("username or password is incorrect, please try again"))
      return redirect('members:login')
    
  
  return render(request, 'registration/login.html')
  
def logout_user(request):
  logout(request)
  messages.success(request, "You have logged out successfully.")
  return redirect('members:login')
  
@login_required
def profile(request):
    return render(request, 'registration/profile.html',{
      'username': request.user.username,
      'email': request.user.email,
      'last_login': request.user.last_login,
    })

@login_required
def members_directory(request):
  query = request.GET.get('q')
  users = User.objects.filter(is_superuser=False)
  if query:
    users = users.filter(username__icontains=query)
    
  paginator = Paginator(users, 3) # Show 3 users per page
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  return render(request, 'tem_members/directory.html', {
    'page_obj': page_obj,
    'query': query,

  })



def contact_view(request):
  if request.method == 'POST':
    form = FeedbackForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Thank you for your feeedback!")
      return redirect('member:contact')
  else:
    form = FeedbackForm()
  return render(request, 'tem_members/contact.html', {'form': form})

@staff_member_required
def feedback_list(request):
    feedbacks = Feedback.objects.order_by('-submitted_at')
    return render(request, 'tem_members/feedback_list.html', {'feedbacks': feedbacks})


# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'], 
#     'firstname': 'BabyE',  
#   }
#   return HttpResponse(template.render(context, request))
# Create your views here.
