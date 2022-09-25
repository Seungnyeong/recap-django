from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "rooms",
        "owner",
        "kind",
        "created_at",
        "updated_at",
    )
    list_filter = ("country", "city", "price", "rooms", "pet_friendly", "amenities")


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    list_filter = ("name", "description", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")