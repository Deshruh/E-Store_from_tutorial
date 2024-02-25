from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from users import forms
from products.models import Basket


def login(request):
    if request.method == "POST":
        form = forms.UserLoginForm(data=request.POST)
        if form.is_valid:
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))

    else:
        form = forms.UserLoginForm()

    context = {"form": form}
    return render(request, "users/login.html", context=context)


def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(data=request.POST)
        if form.is_valid():
            print(form["username"].value)
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = forms.UserRegistrationForm()
    context = {"form": form}
    return render(request, "users/register.html", context=context)


@login_required
def profile(request: HttpRequest):
    if request.method == "POST":
        form = forms.UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = forms.UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    context = {
        "title": "Store - Профиль",
        "form": form,
        "baskets": baskets,
        "total_sum": sum(basket.sum() for basket in baskets),
        "total_quantity": sum(basket.quantity for basket in baskets),
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))
