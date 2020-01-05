from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    url(r'^favicon.ico$', views.return_favicon_ico, name = 'favicon'),  # 获得favicon.ico
    url(r'api/gettingMaze', views.getting_maze, name = 'getting_maze')
]
