from django import forms
from django.forms import Textarea
from django.db.models import Q
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

	class Meta:
		model = StoreInventory
		fields = ['broadSizeCategory', 'strSpecial', 'strUnitType']

	# @property
	# def dstnct(self):
	# 	parent = super().qs
	# 	storeint = getattr(self.request, 'intprop', None)
	# 	storesp = getattr(self.request, 'strSpecial', None)

	# 	return parent.exclude(intprop = '94') 