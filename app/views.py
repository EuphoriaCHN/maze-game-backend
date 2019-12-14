from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import *


# Create your views here.

@require_GET
def index(request):
    """
    Demo Index
    :param request: Http request object
    :return: Template view
    """
    return render(request, 'app/index.html', None)


@require_GET
def return_favicon_ico(request):
    """
    Get favicon.ico
    :param request: Http request object
    :return: image
    """
    try:
        with open("static/favicon.ico", 'rb') as file:
            image_data = file.read()
        return HttpResponse(image_data, content_type = "image/png")
    except Exception as exception:
        print(exception)
        return HttpResponse(str(exception))


@require_POST
def getting_maze(request):
    """
    Get maze from frontend, using BFS to search answer.
    The maze consists of a two-dimensional array of N rows and m columns,
    Each item of the array is a character, and the optional characters are ' ', '#', 'S', 'G'.

    :param request:
    :return: Http Response for Ajax
    """
    pass
