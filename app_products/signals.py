from django.db.models.signals import pre_save
from django.dispatch import receiver
from app_products.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def handle_product_price(sender, instance, **kwargs):
    
    old_instance = None
    if instance.pk:
        try:
            old_instance = ProductModel.objects.get(pk=instance.pk)
            print(f"Updating product {instance.pk}")
            print(f"Old Discount Price: {old_instance.discount_price}, New Price: {instance.price}")
        except ProductModel.DoesNotExist:
            pass  

    
    if instance.discount:
        instance.discount_price = instance.price - (instance.price * instance.discount / 100)
    else:
        instance.discount_price = instance.price
