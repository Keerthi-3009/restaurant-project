from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem, Reservation


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    CATEGORY_TAGLINES = {
        'starters': 'Something delicious to begin with',
        'soups': 'Warm bowls to start your meal',
        'shawarma': 'Fresh, juicy and full of flavour',
        'biryani': 'Fragrant rice layered with spices',
        'meals': 'A complete, satisfying plate',
        'mandhi': 'Traditional Arabian style, slow cooked',
        'main_course': 'The heart of your dining experience',
        'desserts': 'A sweet ending to your meal',
        'beverages': 'Refreshing drinks to go with your food',
    }
    NO_FOOD_TYPE = {'desserts', 'beverages'}

    items = MenuItem.objects.filter(is_available=True).order_by('category', 'food_type', 'name')

    categories = []
    for value, label in MenuItem.CATEGORY_CHOICES:
        dishes = [i for i in items if i.category == value]
        if dishes:
            categories.append({
                'value': value,
                'label': label,
                'tagline': CATEGORY_TAGLINES.get(value, ''),
                'show_food_type': value not in NO_FOOD_TYPE,
                'dishes': dishes,
            })

    return render(request, 'restaurant/menu.html', {'categories': categories})


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