from django.shortcuts import render

def about(request):
    return render(request,"fabric/about.html")

def branches(request):
     return render(request, 'fabric/branches.html')

def branch_detail(request, city):
    city = city.lower()

    if city == 'london':
        return render(request, 'fabric/branches/london.html')
    elif city == 'paris':
        return render(request, 'fabric/branches/paris.html')
    else:
        return render(request, 'fabric/branch_not_found.html')
    
def contacts(request):
    return render(request, 'fabric/contacts.html')

def home(request):
    return render(request, 'fabric/home.html')

def management(request):
    return render(request,'fabric/managment.html')

def news(request):
     return render(request, 'fabric/news.html')

