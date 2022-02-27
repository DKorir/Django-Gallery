from django.shortcuts import render,redirect
from .models import Category, Location, Photo

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    location = request.GET.get('location')
    photos = Photo.objects.all()    
    category = Category.objects.all()
    location = Location.objects.all()
    context = { 'category': category, 'location':location, 'photos': photos }
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