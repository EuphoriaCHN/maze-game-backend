from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    """
    Demo Index
    :param request: Http request object
    :return: Http response
    """
    return render(request, 'app/index.html', None)


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
