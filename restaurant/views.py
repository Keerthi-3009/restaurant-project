# views.py
from django.contrib import messages
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from .models import Category, MenuItem, Reservation

def home(request):
    return render(request, "restaurant/home.html")

def menu(request):
    available = Prefetch("items", queryset=MenuItem.objects.filter(is_available=True), to_attr="available_items")
    categories = []
    for c in Category.objects.prefetch_related(available):
        if not c.available_items:
            continue
        c.veg_items = [i for i in c.available_items if i.food_type == "veg"]
        c.nonveg_items = [i for i in c.available_items if i.food_type == "nonveg"]
        categories.append(c)
    return render(request, "restaurant/menu.html", {"categories": categories})


def book_table(request):
    if request.method == "POST":
        p = request.POST
        Reservation.objects.create(
            name=p["name"], email=p["email"], phone=p["phone"],
            date=p["date"], time=p["time"], guests=p.get("guests", 2),
            occasion=p.get("occasion", ""),
            special_request=p.get("special_request", "").strip(),
        )
        messages.success(request, "Your table is booked. We will confirm shortly.")
        return redirect("book_table")
    return render(request, "restaurant/book_table.html")