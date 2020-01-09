"""
Django View Layer

Created by Qinhong Wang, 2019-12-14
"""

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import *

from tools.BreadthFirstSearch import breadth_first_search
from tools.MakeRandomMaze import build_twist


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
    The maze consists of a two-dimensional array of n rows and m columns,
    Calling BreadthFirstSearch.breadth_first_search(maze, start, end) to get moving step queue and return.
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
    """
    Get the number of rows and columns of the maze that should be generated from the front end,
    use the build twist() function to randomly generate and return a matrix composed of "0" and "1".
    :param request: Http Request
    :return: Http Response for Ajax
    """
    rows = int(request.POST.get('rowNumber'))
    cols = int(request.POST.get('colNumber'))

    if rows & 0x1 is 0 or cols & 0x1 is 0:
        response = {
            "status": 500,
            "data": "错误的迷宫行数或列数！"
        }
    else:
        response = {
            "status": 200,
            "data": build_twist(rows, cols)
        }



    return JsonResponse(response, safe = False)
