from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Store, StoreInventory
from .filters import StoreInventoryFilter

def index(request):
    return HttpResponse("Hello, world!")

def test(request):
	all_stores = Store.objects.all()
	all_store_inventories = StoreInventory.objects.all()
	template = loader.get_template('storage/index.html')
	f = StoreInventoryFilter(request.GET, queryset=StoreInventory.objects.all())
	context = {
        'all_stores': all_stores,
        'all_store_inventories': all_store_inventories
    }
	return render(request, 'storage/index.html', {'filter': f})