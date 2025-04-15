from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('create-profile/', views.create_profile_view, name='create_profile'),
    path('view-profile/', views.view_profile_view, name='view_profile'),
    ]
