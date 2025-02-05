from django.db import models

# Model for laptops.
class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage_capacity = models.CharField(max_length=50)
    max_storage_capacity = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    max_ram_upgrade = models.CharField(max_length=50)
    supported_os = models.CharField(max_length=100)
    battery_health = models.CharField(max_length=50)
    battery_backup = models.CharField(max_length=50)
    screen_size = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    graphics_type = models.CharField(max_length=100)
    total_graphics_memory = models.CharField(max_length=50)
    dedicated_video_memory = models.CharField(max_length=50)
    shared_system_memory = models.CharField(max_length=50)
    hdmi = models.BooleanField(default=False)
    webcam = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    keypad_light = models.BooleanField(default=False)
    touchscreen = models.BooleanField(default=False)
    optical_drive = models.BooleanField(default=False)
    usb_ports = models.CharField(max_length=50)
    vga_output = models.BooleanField(default=False)
    sd_card_reader = models.BooleanField(default=False)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model}"

# Model for laptop images.
class LaptopImages(models.Model):
    laptop = models.ForeignKey(Laptop, related_name='images', on_delete=models.CASCADE)
    img_1 = models.ImageField(upload_to='laptop_images/', blank=True, null=True)
    img_2 = models.ImageField(upload_to='laptop_images/', blank=True, null=True)
    img_3 = models.ImageField(upload_to='laptop_images/', blank=True, null=True)
    img_4 = models.ImageField(upload_to='laptop_images/', blank=True, null=True)
    img_5 = models.ImageField(upload_to='laptop_images/', blank=True, null=True)
    img_6 = models.ImageField(upload_to='laptop_images/', blank=True, null=True)

    def __str__(self):
        return f"Images for {self.laptop.brand} {self.laptop.model}"