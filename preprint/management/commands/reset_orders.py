from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from preprint.models import Order, OrderFile  

class Command(BaseCommand):
    help = 'Reset all orders and files'

    def handle(self, *args, **options):
        orders = Order.objects.all()
        
        for order in orders:
            order_files = OrderFile.objects.filter(order=order)
            
            for order_file in order_files:
                if default_storage.exists(order_file.file.name):
                    default_storage.delete(order_file.file.name)
            
            order.delete()

        self.stdout.write(self.style.SUCCESS('Successfully reset all orders and files.'))
