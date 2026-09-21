from django.shortcuts import render

def favorites_page(request):
    return render(request, 'favorites.html')

