from django.shortcuts import render

def index(request):
    return render(request, "base.html")

def book_search(request):
    search = request.GET.get("search")
    return render(request, "searchresults.html", {"search":search})
