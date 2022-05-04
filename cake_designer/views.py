from django.shortcuts import render
from .forms import GetPhone

def get_number(request):
    if request.method == 'POST':
        form = GetPhone(request.POST)
        if form.is_valid():
            input("YEEEAAAAHHHH")
            return 


def index(request):

    some_data = {
        'Levels'
    }
    context = {
        'DATA': some_data
    }
    return render(request, 'index.html', context)


def lk(request):
    
    context = {
        
    }
    return render(request, 'index.html', context)
