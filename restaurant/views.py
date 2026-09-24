from django.shortcuts import render, redirect
from .models import MenuItem, Reservation

def home(request):
    return render(request, 'home.html')


def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})


def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        # ✅ Validation
        if all([name, email, phone, date, time, guests]):
            Reservation.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                guests=guests,
            )
            return redirect('reservation')  # works if URL is defined

        else:
            return render(request, 'book_table.html', {
                'error': 'All fields are required'
            })

    return render(request, 'book_table.html')