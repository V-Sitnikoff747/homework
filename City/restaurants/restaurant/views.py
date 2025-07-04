from django.shortcuts import render
from . models import Restaurant
from . forms import RestaurantForm
from django.shortcuts import get_object_or_404, redirect

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

def delete_restaurant(request, pk):
    restaurant= get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return redirect("restaurant_list")

def edit_restaurant(request, pk):
    restaurant= get_object_or_404(Restaurant, pk=pk)
    if request.method== 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect("restaurant_list")
    else:
         form = RestaurantForm(instance=restaurant)
         return render(request, 'restaurants/add_edit_restaurant.html', {'form': form})
    

def search_restaurants(request):
    query= request.GET.get('q')
    results = Restaurant.objects.filter(specialization__icontains=query) if query else []
    return render(request, 'restaurants/search.html', {'results': results, 'query': query})

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/add_edit_restaurant.html', {'form': form})