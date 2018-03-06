from django.shortcuts import render, redirect
from urllib.parse import quote_plus

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Room
from .forms import RoomForm

def main_view(request):
    rooms = Room.objects.all()
    form = RoomForm(request.POST or None)
    if form.is_valid():
        room_obj = None
        room_id = int(request.POST.get("room_id"))
        if room_id:
            room_qs = Room.objects.filter(id=room_id)
            if room_qs.exists() and room_qs.count() == 1:
                room_obj = room_qs.first()
        if room_obj:
            room_obj.booked += 1
            room_obj.user.append(request.user.id)
            room_obj.change_date.append(timezone.now())
            room_obj.end_date = form.cleaned_data.get("end_date")
            room_obj.save()
            print(room_obj.booked)
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
    }
    return render(request, "main.html", context)