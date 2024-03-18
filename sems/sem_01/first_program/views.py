from django.http import HttpResponse
import logging

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

LOGGER = logging.getLogger(__name__)


def index(request):
    side = request.GET.get('side')
    LOGGER.debug('side: %s', side)
    # title_page = """<!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>Title</title>
    # </head>
    # <body>
    #
    # <p>Главная</p>
    # <a href="about">Push for About page</a>
    #
    # </body>
    # </html>"""
    #     return HttpResponse(title_page, side)
    return HttpResponse(render(request, 'index.html'), side)


def about(request):
    side = request.GET.get('side')
    LOGGER.debug('side: %s', side)
#     about_page = """<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>About us</title>
# </head>
# <body>
#
# <p>About</p>
#
# </body>
# </html>"""
#     return HttpResponse(about_page, side)
    return HttpResponse(render(request, 'about.html'), side)

