from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Store, StoreInventory
from .filters import StoreInventoryFilter

def index(request):
	template = loader.get_template('storage/index.html')
	f = StoreInventoryFilter(request.GET, queryset=StoreInventory.objects.all())
	return render(request, 'storage/index.html', {'filter': f})