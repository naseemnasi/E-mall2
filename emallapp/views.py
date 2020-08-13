from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from emallapp.forms import regForm, payForm, productForm
from emallapp.models import Register, payment, Category, product


# Create your views here.

def register(request):
    print("new")
    form = regForm()
    if request.method == 'POST':
        print("called")
        form = regForm(request.POST, request.FILES)
        print("ok")
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            return HttpResponse("*****ERROR IN VALIDATION******")
    return render(request, 'register.html', {"form": form})


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, 'index.html')


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {"categories": categories})


def cart(request):
    if request.method == 'POST':
        return redirect('pay')
    return render(request, 'cart.html')


def payment(request):
    print("enter to 11111111111")
    form = payForm()
    if request.method == 'POST':
        print("enter to 222222222222222222")
        form = payForm(request.POST, request.FILES)
        if form.is_valid():
            print("enter to 3333333333333333333333")
            form.save()
            return redirect('finale')
        # else:
        #     return("*****ERROR IN VALIDATION******")
    return render(request, 'payment.html', {"form": form})


def finale(request):
    return render(request, 'finale.html')


def adminpro(request):
    print("new")
    form = productForm()
    if request.method == 'POST':
        print("called")
        form = productForm(request.POST, request.FILES)
        print("ok")
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("*****ERROR IN VALIDATION******")
    return render(request, 'addpro.html', {"form": form})

def vegfruit(request):
    pro = product.objects.all()
    return render(request, 'vegfruit.html', {"product":pro})