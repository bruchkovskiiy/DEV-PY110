from django.shortcuts import render


def wishlist_view(request):
    if request.method == "GET":
        return render(request, 'app_wishlist/wishlist.html', {}) # TODO прописать отображение избранного. Путь до HTML - app_wishlist/wishlist.html
