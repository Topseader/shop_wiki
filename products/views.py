from django.shortcuts import render
from .models import WiredMicrophone
from .models import Brand

def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def product_detail(request, *args, **kwargs):    
    obj = WiredMicrophone.objects.get(id=1).__dict__   
    obj['brand'] = Brand.objects.get(id=obj['brand_id'])

    keys_to_remove = ['_state', 'brand_id', 'id']
    for key in keys_to_remove:
        del obj[key]

    product_info ={'object': obj}

    return render(request, "product/detail.html", product_info)
