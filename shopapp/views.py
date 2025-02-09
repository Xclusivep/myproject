from django.shortcuts import render
from .models import Categories,product,customer,Blog



# Create your views here.
def home(request):

    return render(request,'shop_app/index.html')

def blog01(request):
   return render(request, 'shop_app/blog-detail.html')

def home02(request):
    return render(request,'shop_app/home-2.html')

def home03(request):
    return render(request, 'shop_app/home-3.html')

def home04(request):
    return render(request, 'shop_app/home-4.html')

def home05(request):
    return render(request, 'shop_app/home-5.html')

def Donors(request):
    category = Categories.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'donors.html', context)

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    context1 = {
        'blogs': blogs
    }
    return render(request,'shop_app/blog-list-left-sidebar-1.html', context1 )

def blog_grid(request):
    return render(request, 'shop_app/blog-grid-full-width.html')

def blog_list2(request):
    return render(request, 'shop_app/blog-list-left-sidebar-2.html')
