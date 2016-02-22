import os
import sys

from django.conf import settings


DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 'gywf&aail+k%@00wx#0pzqb8-6gx)3v9=$v!(6wdz7@b2yuo64')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib', 
        'django.contrib.staticfiles',

        'django_ajax',
    ),
    TEMPLATE_DIRS=(
        os.path.join(BASE_DIR, 'templates'),
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    STATIC_URL='/static/',
    STATIC_ROOT='_build/',
)


import time

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.shortcuts import render

from django_ajax.decorators import ajax


@ajax
def my_ajax_view(request):
    time.sleep(10) # Simulate a heavy process
    return {'ajax_text': 'This text is from AJAX.'}


def index(request):
    context = {'text': 'Hola Mundo.'}
    return render(request, 'home.html', context)


urlpatterns = (
    url(r'ajax_text/$', my_ajax_view, name='ajax_text'),
    url(r'$', index, name='homepage'),
)


application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)