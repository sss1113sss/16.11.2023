from django.shortcuts import render   
from django.http import HttpResponse
from .models import Product
# Create your views here.

def main(request):
    content=Product.objects.all
    return render(request=request,template_name='index.html',context=content)