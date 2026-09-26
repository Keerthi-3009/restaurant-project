from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem, Reservation


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    NO_SPLIT_CATEGORIES = {'desserts', 'beverages'}

    items = MenuItem.objects.filter(is_available=True).order_by('category', 'food_type', 'name')
    grouped = {}
    for item in items:
        cat_label = item.get_category_display()
        if item.category in NO_SPLIT_CATEGORIES:
            grouped.setdefault(cat_label, {'flat': []})
            grouped[cat_label]['flat'].append(item)
        else:
            grouped.setdefault(cat_label, {'veg': [], 'non_veg': []})
            grouped[cat_label][item.food_type].append(item)
    return render(request, 'restaurant/menu.html', {'grouped_items': grouped})


def book_table(request):
    if request.method == 'POST':
        Reservation.objects.create(
            name=request.POST.get('name', ''),
            phone=request.POST.get('phone', ''),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            guests=request.POST.get('guests') or 2,
            occasion=request.POST.get('occasion', ''),
            special_request=request.POST.get('message', ''),
        )
        messages.success(request, "Your table has been booked! We'll see you soon.")
        return redirect('book_table')
    return render(request, 'restaurant/book_table.html')