from django.shortcuts import render
from .models import List


# Create your views here.

def all_lists(request):
    all_lists = List.objects.all()

    context = {
        'lists': all_lists,
    }

    return render(request, 'lists/home.html', context)