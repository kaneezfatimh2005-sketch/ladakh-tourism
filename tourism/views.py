from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse

def home(request):
    places = Place.objects.all()
    return render(request, "home.html", {"places": places})


def search_place(request):
    query = request.GET.get("q", "")
    results = Place.objects.filter(name__icontains=query) if query else []
    return render(request, "search.html", {"query": query, "results": results})

def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)
    return render(request, "place_detail.html", {"place": place})

def head(request):
    return render(request, "head.html")
def suggest_places(request):
    query = request.GET.get("q", "").strip()
    if query:
        Places=Place.objects.filter(name__icontains=query)[:8]
        suggestions=[p.name for p in Places]
    else:
        suggestions=[]
    return JsonResponse( suggestions,safe=False)