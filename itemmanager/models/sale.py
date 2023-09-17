from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone

class SaleManager(models.Model):
    pass


class Sale(models.Model):
    user_on_duty = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(default=timezone.now)

    objects = SaleManager()

    def __str__(self):
        return super().__str__()
    

    @property
    def revenue(self):
        from itemmanager.models.saleitem import SaleItem
        profit = SaleItem.objects.sale_total_revenue(sale=self)
        return profit

    '''

    @property
    def revenue(self):
        from itemmanager.models.saleitem import SaleItem
        sale_items = SaleItem.objects.filter(sale=self)
        total_revenue = sum(item.sale_price * item.sale_amount for item in sale_items)
        return total_revenue
    
    '''