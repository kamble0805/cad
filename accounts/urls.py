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
    path('register-vehicle/', views.register_vehicle, name='register_vehicle'),
    path('view-vehicles/', views.view_vehicles, name='view_vehicles'),
    path('vehicle/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
]

