from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'graph.html')

def play_count_by_month(request):
    data = {"month": "2014-01-01", "count_items":"3"}
    return JsonResponse(list(data), safe=False)