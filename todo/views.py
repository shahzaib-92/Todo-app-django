from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseBadRequest

# Create your views here.


def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            itemList = List.objects.all()
            messages.success(request, ("Item has been added to list!"))
            return render(request, "index.html", {"itemList": itemList})
    else:
        itemList = List.objects.all()
        return render(request, "index.html", {"itemList": itemList})


def delete(request, id):
    item = get_object_or_404(List, pk=id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect("index")


def check(request, id):
    item = get_object_or_404(List, pk=id)
    item.isCompleted = True
    item.save()
    return redirect("index")


def uncheck(request, id):
    item = get_object_or_404(List, pk=id)
    item.isCompleted = False
    item.save()
    return redirect("index")


def edit(request, id):
    if request.method == "POST":
        item = get_object_or_404(List, pk=id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ("Item has been updated!"))
            return redirect("index")
    else:
        item = get_object_or_404(List, pk=id)
        return render(request, "edit.html", {"itemee": item})


