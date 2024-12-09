from django.shortcuts import render, get_object_or_404, redirect
from .models import List, Item
from .forms import ListForm, ItemForm
from django.forms import modelform_factory
from django.contrib import messages


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