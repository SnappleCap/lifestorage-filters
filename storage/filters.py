from django import forms
from django.forms import Textarea
from django.db.models import Q, F, Min, Max, Sum, Count
import django_filters
from .models import Store, StoreInventory
from django_filters import rest_framework as filters

SIZE_CHOICES = (
	('Small', 'Small'),
	('Medium', 'Medium'),
	('Large', 'Large'),
)

SPECIALS_CHOICES = (
	('', 'Specials'),
)

CC_CHOICES = (
	('ST-CC', 'Climate Control'),
)

FTR_CHOICES = (
	(-1, 'Free Truck Rental'),
)

class StoreInventoryFilter(django_filters.FilterSet):
	broadSizeCategory = filters.MultipleChoiceFilter(label='', choices=SIZE_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'onclick':'this.form.submit()'}))
	strSpecial = filters.MultipleChoiceFilter(label='', choices=SPECIALS_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'onclick':'this.form.submit()'}), exclude=True)
	strUnitType = filters.MultipleChoiceFilter(label='', choices=CC_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'onclick':'this.form.submit()'}))
	ftruckrental = filters.MultipleChoiceFilter(method='truck_rental_filter', label='', choices=FTR_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'onclick':'this.form.submit()'}))

	class Meta:
		model = StoreInventory
		fields = ['broadSizeCategory', 'strSpecial', 'strUnitType', 'dblTtlAvail']

	def truck_rental_filter(self, queryset, name, value):
		return queryset.filter(
			Q(intprop__ftruckrental__exact='-1') | Q(intprop__ftruckrentalss__exact='-1')
		)

	@property
	def dstnct(self):
		test = super().qs

		return test.values('intprop__storeid').order_by().annotate(Count('intprop'), Min('dblcurrentrate'), Max('strSpecial'), address=F('intprop__address'), city=F('intprop__city'), st=F('intprop__st'), phone=F('intprop__phone'), postalcode=F('intprop__postalcode'), storenum=F('intprop__storeid')).exclude(dblTtlAvail__exact=0)