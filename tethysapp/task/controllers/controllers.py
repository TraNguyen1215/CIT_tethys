from django.shortcuts import render # type: ignore
from tethys_sdk.routing import controller # type: ignore
from tethys_sdk.gizmos import Button # type: ignore

@controller
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'task/home.html', context)

@controller(url='about', method = 'GET')
def about(request, method = "POST"):
    """
    Controller for the app about page.
    """
    context= {}
    return render(request, 'task/about.html',context)