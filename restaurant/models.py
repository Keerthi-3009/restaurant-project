from django.db import models


class MenuItem(models.Model):
    # Edit this list to add/remove/rename categories to match your own menu.
    # Each tuple is ('value_stored_in_db', 'Label_shown_to_people').
    CATEGORY_CHOICES = [
        ('starters', 'Starters'),
        ('soups', 'Soups'),
        ('shawarma', 'Shawarma Fest'),
        ('biryani', 'Biryani'),
        ('meals', 'Meals'),
        ('mandhi', 'Mandhi'),
        ('main_course', 'Main Course'),
        ('desserts', 'Desserts'),
        ('beverages', 'Beverages'),
    ]

    FOOD_TYPE_CHOICES = [
        ('veg', 'Veg'),
        ('non_veg', 'Non-Veg'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='starters')
    food_type = models.CharField(max_length=10, choices=FOOD_TYPE_CHOICES, default='veg')
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=2)
    occasion = models.CharField(max_length=50, blank=True)
    special_request = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"