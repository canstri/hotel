from django.shortcuts import render, redirect
from urllib.parse import quote_plus

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Room, Note
from .forms import RoomForm

def main_view(request):
    rooms = Room.objects.all()
    form = RoomForm(request.POST or None)
    if form.is_valid():
        room_obj = None
        room_id = int(request.POST.get("room_id"))
        
        print("eee") 
        if room_id:
            room_qs = Room.objects.filter(id=room_id)
            if room_qs.exists() and room_qs.count() == 1:
                room_obj = room_qs.first()
        if room_obj:
            if room_obj.booked == 1000:
                room_obj.booked = 0
            room_obj.booked += 1
            room_obj.save()
        free = False
        if room_obj.booked % 2 == 0:
            free = True
        c = Note.objects.get_or_create(
            user = str(request.user),
            room = room_id,
            booked = free,
            timestamp = timezone.now(),
        )
        return HttpResponseRedirect("main") 


    staff = "no"
    if request.user.is_staff:
        staff = "yes"
    admin = "no"
    if request.user.is_superuser:
        admin = "yes"
    context = {
        "admin": admin,
        "staff": staff,
        "rooms": rooms,
        "form": form,
        "user":request.user,        
    }
    return render(request, "main.html", context)
def table(request):
    notes = Note.objects.all()
    admin = "no"
    if request.user.is_superuser:
        admin = "yes"
    staff = "no"
    if request.user.is_staff:
        staff = "yes"

    context = {
        "admin": admin,
        "staff": staff,
        "user":request.user,
        "notes":notes,
    }
    return render(request, "table.html", context)
