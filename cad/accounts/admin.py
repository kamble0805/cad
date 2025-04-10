from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'occupation')  # shown in list view
    search_fields = ('first_name', 'last_name', 'phone_number', 'aadhaar_number')     # adds search box
    list_filter = ('occupation', 'gender')                                            # sidebar filters
