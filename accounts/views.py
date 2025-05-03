from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Vehicle


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'accounts/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'accounts/login.html')
@login_required
def create_profile_view(request):
    if request.method == 'POST':
        UserProfile.objects.create(
            user=request.user,
            aadhaar_number=request.POST.get('aadhaar_number'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),
            phone_number=request.POST.get('phone_number'),
            occupation=request.POST.get('occupation'),
            address=request.POST.get('address'),
            profile_picture_url=request.POST.get('profile_picture_url')
        )
        messages.success(request, 'Profile created successfully!')
        return redirect('dashboard')

    return render(request, 'accounts/create_profile.html')







@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def view_profile_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
        return render(request, 'accounts/view_profile.html', {'profile': profile})
    except UserProfile.DoesNotExist:
        messages.warning(request, "You haven't created a profile yet. Please complete your profile to continue.")
        return redirect('create_profile')  # Make sure this name exists in urls.py




def index(request):
    return render(request, 'index.html')



# ✅ Register Vehicle
@login_required
def register_vehicle(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')

    if request.method == 'POST':
        vehicle_name = request.POST.get('vehicle_name')
        vehicle_type = request.POST.get('vehicle_type')
        registration_number = request.POST.get('registration_number')

        Vehicle.objects.create(
            owner_profile=user_profile,
            vehicle_name=vehicle_name,
            vehicle_type=vehicle_type,
            registration_number=registration_number
        )
        messages.success(request, "Vehicle registered successfully.")
        return redirect('view_vehicles')

    return render(request, 'accounts/register_vehicle.html')


# ✅ View All Vehicles
@login_required
def view_vehicles(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')

    vehicles = Vehicle.objects.filter(owner_profile=user_profile)

    if not vehicles.exists():
        messages.warning(request, "No vehicle registered. Please register one.")
        return redirect('register_vehicle')

    return render(request, 'accounts/view_vehicles.html', {'vehicles': vehicles})


# ✅ View Vehicle Details
@login_required
def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, owner_profile__user=request.user)
    return render(request, 'accounts/vehicle_detail.html', {'vehicle': vehicle})

