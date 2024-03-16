from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

""" def january(request):
    return HttpResponse("This january page !")


def february(request):
    return HttpResponse("This is february Page ! ")

def march(request):
    return HttpResponse("This is March Page !") """
    
monthly_challenges = {
    "january" : "This is january Page ! " ,
    "february" : "This is february Page ! " ,
    "march" : "This is march Page ! " ,
    "april" : "This is april Page ! " ,
    "may" : "This is may Page ! " ,
    "june" : "This is june Page ! " ,
    "july" : "This is january Page ! " ,
    "august" : "This is august Page ! " ,
    "september" : "This is september Page ! " ,
    "october" : "This is october Page ! " ,
    "november" : "This is november Page ! " ,
    "december" : None ,
    
}    

""" def monthly_challeges_by_number(request, month):
    return HttpResponse(month) """
""" def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data) """
    
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })    
    
    
def monthly_challeges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month number")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

""" def monthly_challeges(request, month):
    challeges_text = None
    if month == "january":
        challeges_text = "This is january page !"
        
    elif month == "february":
        challeges_text = "This is february page !"
    
    elif month == "march":
        challeges_text = "This is march page !"
        
    else:
        return HttpResponseNotFound("This month is not supported")
    
    return HttpResponse(challeges_text) """
    
    
""" def monthly_challeges(request, month):
    try:
        challeges_text = monthly_challenges[month]
        return HttpResponse(challeges_text)
    except:
        return HttpResponseNotFound("This month is not supported") """
    
def monthly_challeges(request, month):
    try:
        challeges_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text" : challeges_text,
            "month_name" : month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)   
           
        
    
    