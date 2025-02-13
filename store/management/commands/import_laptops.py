import json
from django.core.management.base import BaseCommand
from store.models import Laptop

class Command(BaseCommand):
    help = 'Import laptops from JSON file'

    def handle(self, *args, **kwargs):
        with open('laptops_data.json') as f:
            data = json.load(f)

            for item in data:
                Laptop.objects.create(
                    img_1=item['img_1'],
                    img_2=item['img_2'],
                    img_3=item['img_3'],
                    img_4=item['img_4'],
                    img_5=item['img_5'],
                    img_6=item['img_6'],
                    brand=item['brand'],
                    model=item['model'],
                    processor=item['processor'],
                    storage_capacity=item['storage_capacity'],
                    ram=item['ram'],
                    supported_os=item['supported_os'],
                    battery_health=item['battery_health'],
                    battery_backup=item['battery_backup'],
                    screen_size=item['screen_size'],
                    resolution=item['resolution'],
                    graphics_type=item['graphics_type'],
                    total_graphics_memory=item['total_graphics_memory'],
                    dedicated_video_memory=item['dedicated_video_memory'],
                    shared_system_memory=item['shared_system_memory'],
                    hdmi=item['hdmi'],
                    webcam=item['webcam'],
                    wifi=item['wifi'],
                    keypad_light=item['keypad_light'],
                    touchscreen=item['touchscreen'],
                    optical_drive=item['optical_drive'],
                    vga_output=item['vga_output'],
                    sd_card_reader=item['sd_card_reader'],
                    usb_ports=item['usb_ports'],
                    condition=item['condition'],
                    price=item['price'],
                    discount=item['discount'],
                    available=item['available'],
                )
        self.stdout.write(self.style.SUCCESS('Laptops imported successfully'))
