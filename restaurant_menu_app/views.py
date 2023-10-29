from django.shortcuts import render, redirect
from restaurant_menu_app.models import MenuItem, Category
from restaurant_menu_app.forms import MenuItemForm

def menu_list(request):
    categories = Category.objects.all()

    return render(request, 'restaurant_menu_app/menu_list.html', {'categories': categories})

def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant_menu_app:menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'restaurant_menu_app/menu_form.html', {'form': form})

def edit_menu_item(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('restaurant_menu_app:menu_list')
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, 'restaurant_menu_app/menu_form.html', {'form': form})

def remove_menu_item(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    menu_item.delete()
    return redirect('restaurant_menu_app:menu_list')