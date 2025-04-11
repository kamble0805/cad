from django.contrib import admin
from .models import UserProfile
from .models import Vehicle

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'occupation')  # shown in list view
    search_fields = ('first_name', 'last_name', 'phone_number', 'aadhaar_number')     # adds search box
    list_filter = ('occupation', 'gender')                                            # sidebar filters


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_plate', 'vehicle_model', 'vehicle_type', 'owner_name', 'registration_date')
    search_fields = ('vehicle_plate', 'vehicle_model', 'vehicle_type', 'owner_profile__aadhaar_number')
    list_filter = ('vehicle_type', 'vehicle_color', 'registration_date')

    def owner_name(self, obj):
        return f"{obj.owner_profile.first_name} {obj.owner_profile.last_name}"
    owner_name.short_description = 'Owner Name'