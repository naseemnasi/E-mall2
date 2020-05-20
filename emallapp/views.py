from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from emallapp.forms import regForm
from emallapp.models import Register


# Create your views here.
def index(request):
    return render(request, 'index.html')


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
    return render(request, 'cart.html')


def payment(request):
    return render(request, 'payment.html')


def finale(request):
    return render(request, 'finale.html')

