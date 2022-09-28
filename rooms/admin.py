import re
from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="모든 Price를 0으로 만듬")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "rooms",
        "owner",
        "total_amenities",
        "rating",
        "kind",
        "created_at",
    )
    list_filter = ("country", "city", "price", "rooms", "pet_friendly", "amenities")

    # ^ startwiths
    #     | Prefix | Lookup |
    # | ------ | ---------- |
    # | ^ | startswith |
    # | = | iexact |
    # | @ | search |
    # | None | icontains |
    # | | |
    search_fields = ("^name", "=price", "=owner__username")


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    list_filter = ("name", "description", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
