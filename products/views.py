from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products import models


def index(request):
    context = {"title": "Store"}
    return render(request, "products/index.html", context=context)


def products(request, category_id=None, page=1):
    products = (
        models.Product.objects.filter(category__id=category_id)
        if category_id
        else models.Product.objects.all()
    )
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)

    context = {
        "title": "Store - Каталог",
        "categories": models.ProductCategory.objects.all(),
        "products": products_paginator,
    }

    return render(request, "products/products.html", context=context)


@login_required
def basket_add(request, product_id):
    product = models.Product.objects.get(id=product_id)
    baskets = models.Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        models.Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_id):
    basket = models.Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
