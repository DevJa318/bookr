from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "Świecie"
    return render(request, "base.html", {"name": name, "name2":"Anna"})

