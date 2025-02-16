from django import forms
from .models import Laptop


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = [
            "brand",
            "model",
            "processor",
            "storage_capacity",
            "max_storage_capacity",
            "ram",
            "max_ram_upgrade",
            "supported_os",
            "battery_health",
            "battery_backup",
            "screen_size",
            "resolution",
            "graphics_type",
            "total_graphics_memory",
            "dedicated_video_memory",
            "shared_system_memory",
            "hdmi",
            "webcam",
            "wifi",
            "keypad_light",
            "touchscreen",
            "optical_drive",
            "vga_output",
            "sd_card_reader",
            "usb_ports",
            "condition",
            "price",
            "discount",
            "available",
            "img_1",
            "img_2",
            "img_3",
            "img_4",
            "img_5",
            "img_6",
        ]

        widgets = {
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "processor": forms.TextInput(attrs={"class": "form-control"}),
            "storage_capacity": forms.TextInput(attrs={"class": "form-control"}),
            "max_storage_capacity": forms.TextInput(attrs={"class": "form-control"}),
            "ram": forms.TextInput(attrs={"class": "form-control"}),
            "max_ram_upgrade": forms.TextInput(attrs={"class": "form-control"}),
            "battery_health": forms.TextInput(attrs={"class": "form-control"}),
            "battery_backup": forms.TextInput(attrs={"class": "form-control"}),
            "screen_size": forms.TextInput(attrs={"class": "form-control"}),
            "resolution": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "discount": forms.NumberInput(attrs={"class": "form-control"}),
        }
