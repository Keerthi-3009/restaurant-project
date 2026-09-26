from django.contrib import admin
from .models import MenuItem, Reservation


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)
    list_editable = ('price', 'is_available')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests', 'occasion', 'phone')
    list_filter = ('date', 'occasion')
    search_fields = ('name', 'email', 'phone')
# Order model/admin removed — no ordering flow anymore.