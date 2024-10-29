from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize

def home(request):
    qs = Product.objects.all()
    serialize_data = serialize("json", qs)
    serialize_data = json.loads(serialize_data)
    return JsonResponse(serialize_data, status=200)
