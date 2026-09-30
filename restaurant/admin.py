from django.contrib import admin
from .models import Category, MenuItem, Reservation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "show_food_type")
    list_editable = ("order", "show_food_type")

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "food_type", "price", "is_available")
    list_editable = ("food_type", "price", "is_available")
    list_filter = ("category", "food_type", "is_available")
    search_fields = ("name",)
    fieldsets = (
        (None, {"fields": ("category", "name", "description", "price", "is_available")}),
        ("Veg / Non-veg (ignored for Desserts and Beverages)", {"fields": ("food_type",)}),
        ("Photo (optional)", {"fields": ("image", "image_url")}),
    )

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "time", "guests", "occasion", "phone")
    list_filter = ("date", "occasion")