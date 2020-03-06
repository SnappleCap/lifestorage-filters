from django.db import models
import django_filters
from phone_field import PhoneField

class Store(models.Model):
    intprop = models.IntegerField(primary_key='True')
    phone = PhoneField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    st = models.CharField(max_length=2)
    postalcode = models.IntegerField()
    ftruckrental = models.IntegerField()
    ftruckrentalss = models.IntegerField()
    fdisplay = models.CharField(max_length=200)
    fltInStorePerc = models.DecimalField(max_digits=2, decimal_places=1)
    facq = models.CharField(max_length=200)
    community = models.CharField(max_length=200)


class StoreInventory(models.Model):
    intprop = models.ForeignKey(Store, to_field='intprop', on_delete=models.CASCADE)
    strUnitType = models.CharField(max_length=5)
    strInside = models.CharField(max_length=1)
    dblfloor = models.IntegerField()
    fltInStorePerc = models.DecimalField(max_digits=2, decimal_places=1)
    dblcurrentrate = models.IntegerField()
    dblttlSpaces = models.IntegerField()
    dblTtlAvail = models.IntegerField()
    fineSizeCategory = models.CharField(max_length=200)
    broadSizeCategory = models.CharField(max_length=200)
    strSpecial = models.CharField(max_length=1)

    class Meta:
        ordering = ['intprop', 'dblcurrentrate']