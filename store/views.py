from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop
from .forms import LaptopForm
from django.contrib import messages

def laptop_list(request):
    query = request.GET.get('q')
    brand_filter = request.GET.get('brand')
    condition_filter = request.GET.get('condition')
    
    laptops = Laptop.objects.all()

    if query:
        laptops = laptops.filter(model__icontains=query)

    if brand_filter:
        laptops = laptops.filter(brand=brand_filter)

    if condition_filter:
        laptops = laptops.filter(condition=condition_filter)

    brands = Laptop.objects.values_list('brand', flat=True).distinct()
    conditions = Laptop.objects.values_list('condition', flat=True).distinct()

    return render(request, 'store/laptop_list.html', {
        'laptops': laptops,
        'brands': brands,
        'conditions': conditions
    })


def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, "laptops/laptop_detail.html", {"laptop": laptop})


def laptop_create(request):
    if request.method == "POST":
        form = LaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Laptop added successfully!")
            return redirect("laptop_list")
    else:
        form = LaptopForm()
    return render(request, "laptops/laptop_form.html", {"form": form})


def laptop_update(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == "POST":
        form = LaptopForm(request.POST, request.FILES, instance=laptop)
        if form.is_valid():
            form.save()
            messages.success(request, "Laptop updated successfully!")
            return redirect("laptop_detail", pk=pk)
    else:
        form = LaptopForm(instance=laptop)
    return render(request, "laptops/laptop_form.html", {"form": form})

def laptop_delete(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    laptop.delete()
    messages.success(request, "Laptop deleted successfully!")
    return redirect("laptop_list")
