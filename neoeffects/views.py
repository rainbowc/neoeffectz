from django.shortcuts import render
from .models import ContactUs


# Create your views here.


def home(request):   
    context = {'title':'home'}
    return render(request, 'neoeffects/index.html', context)


def about(request):
    context = {'title':'About Us'}
    return render(request, 'neoeffects/about-us.html', context)

def blog_details(request):
    context = {'title':'Blog Details'}
    return render(request, 'neoeffects/blog-details.html', context)

def blog_masonry(request):
    context = {'title':'Blog'}
    return render(request, 'neoeffects/blog-masonry.html', context)

def blog_standard(request):
    context = {'title':'Blog'}
    return render(request, 'neoeffects/blog-standard.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('content')
        
        
        contact_us = ContactUs.objects.create(
            name=name,
            email=email,
            phone_number = phone_number,
            message=message
        )
        contact_us.save()
    return render(request, 'neoeffects/contact-us.html')

def faq(request):
    context = {'title':'faq'}
    return render(request, 'neoeffects/faq.html', context)


