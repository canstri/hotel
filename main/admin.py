from django.contrib import admin

# Register your models here.
from .models import Room

class RoomModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "booked", "change_date", "end_date"]
    list_display_links = ["id"]
    list_editable = ["booked"]
    list_filter = ["id", "user", "booked"]

    search_fields = ["id", "user"]
    class Meta:
        model = Room


admin.site.register(Room, RoomModelAdmin)