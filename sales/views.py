from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from .helper import *
# Create your views here.

def index(request):
    return render(request,'sales/index.html')

def category(request):
    data = Items.objects.values('category').distinct()
    print(data)
    return render(request,'sales/category.html',{
        'data':data
    })
    
def items(request,cat):
    data = Items.objects.filter(category=cat)
    return render(request,'sales/items.html',{
        'data':data
    })
    
from django.http import JsonResponse
from .models import Items

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        items = Items.objects.filter(name__icontains=query)
        results = list(items.values('name','price','website_link','unit'))  # You can add more fields here
        
        return JsonResponse({'data': results})
    
    


def infinite_scroll(request):
    page_number = request.GET.get('page', 1)
    
    items = Items.objects.all()
    paginator = Paginator(items, 15)  # 10 items per "page"

    page_obj = paginator.get_page(page_number)
    data = list(page_obj.object_list.values('id', 'name', 'price', 'unit', 'website_link'))

    return JsonResponse({
        'data': data,
        'has_next': page_obj.has_next()
    })
    
def help(request):
   return render(request,'sales/help.html')

def about(request):
    return render(request,'sales/about.html')

def recipe(request,lookup):

    Food = food(lookup) 
    instructions = Food.instructions
    img = Food.img
    video = Food.video        
    ingredients = Food.get_ingredients()
        
    return render(request,'sales/recipe.html',{
        'instructions':instructions if instructions else '',
        'img':img if img else '',
        'ingredients':ingredients if ingredients else '',
        'name':lookup,
        'video':video.replace('watch?v=','embed/') if video else ''
        
    })
    
def Form(request):
    cat,img= CATEGORY()
    return render(request,'sales/form.html',{
        'cat':zip(cat,img)

    })
    
def view_meals(request,cat):
    meal,img = ITEM(cat)
    return render(request,'sales/snacks.html',{
        'post': zip(meal,img),
        'cat':cat
    })