from django.urls import path
from . import views


app_name = 'members'

urlpatterns = [
    path('', views.home, name='home'),
    path('myfirst/', views.myfirst, name='myfirst'),
    path('main/', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('testing/', views.testing, name= 'testing'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('syntax/', views.syntax, name='syntax'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('directory/', views.members_directory, name='directory'),
    path('contact/', views.contact_view, name='contact'),
    path('feedbacks/', views.feedback_list, name='feedback_list'),
]