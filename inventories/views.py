from django.shortcuts import render
from .models import *
from stores.models import Store
# Create your views here.

def inventory_list(request, store_id):
	store = Store.objects.get(id=store_id)
	context = {
	"items": store.inventories.all()
	}
	return render(request, "inventory_list.html", context)