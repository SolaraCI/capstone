from django.shortcuts import render, get_object_or_404, redirect
from .models import List, Item
from .forms import ListForm, ItemForm
from django.forms import modelform_factory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def all_lists(request):
    """Retrieves all existing lists to display on home page"""
    all_lists = List.objects.all()

    context = {
        'lists': all_lists,
    }

    return render(request, 'todo/home.html', context)


def view_list(request, list_id):
    """Retrieves selected list and returns it to render"""
    todo_list = get_object_or_404(List, id=list_id)

    context = {
        'list': todo_list,
        'items': todo_list.items,
        'item_names': todo_list.items.values('name'),
    }

    return render(request, 'todo/view_list.html', context)


def create_list(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "List created successfully.")
            return redirect('home')
        else:
            messages.error(request, "ERROR: Could not create list.") 
            return redirect('home')
    else:
        form = ListForm()
        context = {
            "form": form,
        }
        return render(request, 'todo/create_list.html', context)
    

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 4:
            messages.error(request, 'Password must be at least 4 characters')
            return redirect('register')
        
        get_all_user_names = User.objects.filter(username=username)
        if get_all_user_names:
            messages.error(request, 'Username must be unique. Please choose another.')
            return redirect('register')
        
        get_all_user_emails = User.objects.filter(email=email)
        if get_all_user_emails:
            messages.error(request, 'Email address already in use. Please use another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
    return render(request,'todo/register.html', {})




