"""
Django View Layer

Created by Qinhong Wang, 2019-12-14
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import *
from tools.BreadthFirstSearch import breadth_first_search
from tools.MakeRandomMaze import build_twist
import json
from django.core import serializers
import simplejson
import random


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
    Calling BreadthFirstSearch.breadth_first_search(maze, start, end) to get moving step queue and return,
    But before That, this function should find 'S'(Start Point) location and 'G'(Goal Point) location.
    :param request: Http Request
    :return: Http Response for Ajax
    """
    maze = request.POST.get('maze')
    start = request.POST.get('start')
    end = request.POST.get('end')

    maze = eval(maze)
    start = eval(start)
    end = eval(end)

    ans = breadth_first_search(maze, start, end)

    return JsonResponse(ans, safe = False)


@require_POST
def random_maze(request):
    rows = int(request.POST.get('rowNumber'))
    cols = int(request.POST.get('colNumber'))

    if rows & 0x1 is 0 or cols & 0x1 is 0:
        m = []
    else:
        m = build_twist(rows, cols)

    return JsonResponse(m, safe = False)
