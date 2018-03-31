from django.contrib import admin

# Register your models here.
from .models import Room, Note

class RoomModelAdmin(admin.ModelAdmin):
    list_display = ["id", "booked"]
    list_display_links = ["id"]
    list_editable = ["booked"]
    list_filter = ["id", "booked"]

    search_fields = ["id"]
    class Meta:
        model = Room

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ["id", "room", "booked", "user", "timestamp"]
    list_display_links = ["id"]
    list_editable = ["booked"]
    list_filter = ["id", "booked"]

    search_fields = ["id"]
    class Meta:
        model = Note


admin.site.register(Room, RoomModelAdmin)
admin.site.register(Note, NoteModelAdmin)