from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LaptopForm, LaptopImagesFormSet

# Create your views here.
def upload_laptop(request):
    if request.method == 'POST':
        laptop_form = LaptopForm(request.POST, request.FILES)
        laptop_images_formset = LaptopImagesFormSet(request.POST, request.FILES)
        
        if laptop_form.is_valid() and laptop_images_formset.is_valid():
            laptop = laptop_form.save()
            laptop_images_formset.instance = laptop
            laptop_images_formset.save()
            return redirect('success_url')  # Replace 'success_url' with your success URL
    else:
        laptop_form = LaptopForm()
        laptop_images_formset = LaptopImagesFormSet()
    
    return render(request, 'upload_laptop.html', {
        'laptop_form': laptop_form,
        'laptop_images_formset': laptop_images_formset,
    })