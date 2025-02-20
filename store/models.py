from django.db import models
from django.conf import settings


# Choices for Laptop Condition
CONDITION_CHOICES = [
    ("like_new", "Like New"),
    ("good", "Good"),
    ("fair", "Fair"),
]


class Laptop(models.Model):
    img_1 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    img_2 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    img_3 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    img_4 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    img_5 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)
    img_6 = models.ImageField(upload_to="laptop_images/", blank=True, null=True)

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage_capacity = models.CharField(max_length=50, help_text="E.g., 256GB SSD")
    max_storage_capacity = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, help_text="E.g., 8GB DDR4")
    max_ram_upgrade = models.CharField(max_length=50, blank=True, null=True)
    supported_os = models.CharField(max_length=100)
    battery_health = models.CharField(max_length=50)
    battery_backup = models.CharField(max_length=50)
    screen_size = models.CharField(max_length=50, help_text="E.g., 15.6 inches")
    resolution = models.CharField(max_length=50, help_text="E.g., 1920x1080")
    graphics_type = models.CharField(max_length=100, help_text="Integrated / Dedicated")
    total_graphics_memory = models.CharField(max_length=50, blank=True, null=True)
    dedicated_video_memory = models.CharField(max_length=50, blank=True, null=True)
    shared_system_memory = models.CharField(max_length=50, blank=True, null=True)

    hdmi = models.BooleanField(default=False)
    webcam = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    keypad_light = models.BooleanField(default=False)
    touchscreen = models.BooleanField(default=False)
    optical_drive = models.BooleanField(default=False)
    vga_output = models.BooleanField(default=False)
    sd_card_reader = models.BooleanField(default=False)
    usb_ports = models.CharField(max_length=50)

    condition = models.CharField(
        max_length=20, choices=CONDITION_CHOICES, default="good"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Price in USD"
    )
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, help_text="Discount in %"
    )
    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.condition.capitalize()}"


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart - {self.user.email if self.user else 'Guest'}"

    def item_count(self):
        return self.items.count()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    laptop = models.ForeignKey("Laptop", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.laptop.price * self.quantity

    def __str__(self):
        return f"{self.laptop.brand} {self.laptop.model} - {self.quantity}"


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addresses"
    )
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default="Nigeria")  # Default to Nigeria

    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store price at purchase time

    def __str__(self):
        return f"{self.laptop.brand} {self.laptop.model} - {self.quantity}"
