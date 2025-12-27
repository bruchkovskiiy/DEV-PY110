from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotFound
from app_store.models import DATABASE
from django.contrib.auth import get_user
from logic.control_wishlist import view_in_wishlist, add_to_wishlist, remove_from_wishlist
from django.contrib.auth.decorators import login_required


def wishlist_view(request):
    if request.method == "GET":
        username = get_user(request).username
        data = view_in_wishlist(username)[username]  # TODO получить продукты из избранного для пользователя, используя view_in_wishlist

        products = [DATABASE[product_id] for product_id in data['products']]
        # TODO сформировать список словарей продуктов с их характеристиками. Пройдитесь по id продуктам в data
        #  получите словари с характеристиками продуктов по их id и запишите в список products

        return render(request, 'app_wishlist/wishlist.html', context={"products": products})