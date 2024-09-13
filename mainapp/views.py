from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'MainApp.html')
