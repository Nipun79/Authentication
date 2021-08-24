from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from . forms import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(request, "signup not completed")
    else:
        form = RegisterForm()
    return render(request,"accounts/register.html",{"form":form})
