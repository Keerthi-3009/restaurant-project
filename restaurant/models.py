import re
from django.db import models

# Dish word -> photo search tag. Order matters: the first match wins.
NAME_TAGS = [
    ("biryani", "biryani"), ("biriyani", "biryani"), ("pizza", "pizza"), ("burger", "burger"),
    ("mojito", "mojito"), ("colada", "colada"), ("lassi", "lassi"), ("coffee", "coffee"),
    ("tea", "tea"), ("shake", "milkshake"), ("juice", "juice"), ("lemonade", "lemonade"),
    ("mocktail", "mocktail"), ("sparkler", "mocktail"), ("fizz", "mocktail"),
    ("brownie", "brownie"), ("cheesecake", "cheesecake"), ("cake", "cake"), ("kulfi", "kulfi"),
    ("gulab", "gulabjamun"), ("jamun", "gulabjamun"), ("icecream", "icecream"), ("ice", "icecream"),
    ("tikka", "tikka"), ("kebab", "kebab"), ("naan", "naan"), ("soup", "soup"), ("fries", "fries"),
    ("noodles", "noodles"), ("pasta", "pasta"), ("sandwich", "sandwich"), ("salad", "salad"),
    ("prawn", "prawns"), ("fish", "fish"), ("mutton", "mutton"), ("paneer", "paneer"),
    ("curry", "curry"), ("masala", "curry"),
]

# Category name (part of it) -> tag, used when the dish name isn't recognised.
CATEGORY_TAGS = [
    ("starter", "appetizer"), ("main", "curry"), ("biryani", "biryani"), ("pizza", "pizza"),
    ("dessert", "dessert"), ("drink", "mocktail"), ("beverage", "mocktail"),
]

EMOJIS = {
    "biryani": "🍛", "curry": "🍛", "pizza": "🍕", "burger": "🍔", "mojito": "🍹",
    "colada": "🍹", "mocktail": "🍹", "lassi": "🥛", "coffee": "☕", "tea": "☕",
    "milkshake": "🥤", "juice": "🧃", "lemonade": "🍋", "brownie": "🍫", "cake": "🍰",
    "cheesecake": "🍰", "kulfi": "🍨", "gulabjamun": "🍮", "icecream": "🍨",
    "tikka": "🍢", "kebab": "🍢", "naan": "🫓", "soup": "🍲", "fries": "🍟",
    "noodles": "🍜", "pasta": "🍝", "sandwich": "🥪", "salad": "🥗", "prawns": "🍤",
    "fish": "🐟", "mutton": "🍖", "paneer": "🧀", "appetizer": "🥗", "dessert": "🍰",
}

class Category(models.Model):
    name = models.CharField(max_length=80)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")
    show_food_type = models.BooleanField(
        default=True, help_text="Show the Veg / Non-veg marker. Untick for Drinks and Desserts."
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    FOOD_TYPES = [("veg", "Veg"), ("nonveg", "Non-veg")]

    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    food_type = models.CharField(max_length=6, choices=FOOD_TYPES, default="veg")
    image = models.ImageField(upload_to="menu/", blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="Or paste an image link instead of uploading")
    is_available = models.BooleanField(default=True)

    
    def _tag(self):
        words = re.findall(r"[a-z]+", self.name.lower())
        tag = next((t for key, t in NAME_TAGS if key in words), None)
        if not tag:
            cat = self.category.name.lower()
            tag = next((t for key, t in CATEGORY_TAGS if key in cat), "food")
        return tag

    @property
    def photo_url(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return f"https://loremflickr.com/300/300/{self._tag()}?lock={self.pk or 0}"

    @property
    def emoji(self):
        return EMOJIS.get(self._tag(), "🍽️")


class Reservation(models.Model):
    OCCASION_CHOICES = [
        ("Birthday", "Birthday"),
        ("Anniversary", "Anniversary"),
        ("Date night", "Date night"),
        ("Proposal", "Proposal"),
        ("Other celebration", "Other celebration"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    occasion = models.CharField(max_length=40, blank=True, choices=OCCASION_CHOICES)
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"