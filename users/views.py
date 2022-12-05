from django.shortcuts import render ,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from products.models import Cart


def register (req):
    if req.method=='POST':
        form=UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            cart=Cart(user=User.objects.last())
            cart.save()
            return redirect('/login/')
    else:
        form=UserCreationForm()
    return render(req,'users/register.html',{'form':form})

