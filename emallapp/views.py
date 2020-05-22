from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from emallapp.forms import regForm,payForm
from emallapp.models import Register,payment


# Create your views here.
def index(request):
    print("new")
    form = regForm()
    if request.method == 'POST':
        print("called")
        form = regForm(request.POST, request.FILES)
        print("ok")
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("*****ERROR IN VALIDATION******")
    return render(request, 'index.html',{"form":form})


def category(request):
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
    return render(request, 'category.html',{"form":form})


def cart(request):
    return redirect("pay")
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
    return render(request, 'payment.html',{"form":form})


def finale(request):
    return render(request, 'finale.html')
