from unicodedata import category
from django.shortcuts import render,redirect

from .models import Category, Location, Photo
import os
# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    location = request.GET.get('location')
    if category==None:
        photos = Photo.objects.all()    
    else:
        photos = Photo.objects.filter(category__name=category)  
    categories = Category.objects.all()
    location = Location.objects.all()
    context = { 'categories': categories, 'location':location, 'photos': photos }
    return render(request,'photos/gallery.html', context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.object.get_or_create(name=data['category_new'])
        else:
                category = None
        if data['location'] != 'none':
            location = Location.objects.get(id=data['location'])
        elif data['location_new'] != '':
            location, created = Location.object.get_or_create(name=data['location_new'])
        else:
                location = None
        photo = Photo.objects.create(
                category = category,
                location = location,
                description = data['description'],
                image = image,
            )
        return redirect('gallery')
    
    context = { 'categories': categories,'locations': locations}
    return render(request,'photos/add.html', context)



        
    context={'photo': photo}

    return render(request,'photos/update.html', context)


def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos= Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

# def search_results(request):

#     if 'article' in request.GET and request.GET["photo"]:
#         search_term = request.GET.get("photo")
#         searched_photo = Photo.search_by_category(search_term)
#         message = f"{search_term}"

#         return render(request, 'photos/search.html',{"message":message,"photos": searched_photo})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'photos/search.html',{"message":message})

