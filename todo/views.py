from django.shortcuts import render, get_object_or_404, redirect
from .models import List, Item
from .forms import ListForm, ItemForm
from django.forms import modelform_factory
from django.contrib.messages import constants as messages


# Create your views here.

def all_lists(request):
    all_lists = List.objects.all()

    context = {
        'lists': all_lists,
    }

    return render(request, 'todo/home.html', context)


def view_list(request, list_id):
    todo_list = get_object_or_404(List, id=list_id)

    

    context = {
        'list': todo_list,
        'items': todo_list.items,
        'item_names': todo_list.items.values_list("name"),
    }

    return render(request, 'todo/view_list.html', context)


def create_list(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "List created successfully.")
            return redirect('list_home')
        else:
            return redirect('create_list')
    else:
        form - ListForm()
        context = {
            "form": form,
        }
        return render(request, 'todo/create_list.html', context)