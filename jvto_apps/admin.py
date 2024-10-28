from django.contrib import admin

# Register your models here.
from .models import (
    Packages,
    Itineraries
)

class ItineraryInline(admin.TabularInline):
    model = Itineraries
    extra = 0
@admin.register(Packages)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'meta_description', 'departure', 'return_field')
    search_fields = ('name', 'departure', 'return_field')
    inlines = [ItineraryInline]
    list_per_page = 20

# Optional: Register individual models if you need separate management
@admin.register(Itineraries)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('package', 'day', 'title', 'activity')
    list_filter = ('title','activity', 'day')
    search_fields = ('title','activity', 'day')
    list_per_page = 20

# class AccommodationInline(admin.TabularInline):
#     model = Accommodation
#     extra = 0

# class CrewAssignmentInline(admin.TabularInline):
#     model = CrewAssignment
#     extra = 0

# class VehicleAssignmentInline(admin.TabularInline):
#     model = VehicleAssignment
#     extra = 0
