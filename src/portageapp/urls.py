"""portageapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inputs.views import input_single_view, input_list_view, input_new_view
from outputs.views import output_single_view, output_list_view
from pages.views import home_view, apply_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'users/', include('django.contrib.auth.urls')),
    url(r'inputs/(?P<input_id>\d+)/$', input_single_view, name = 'inputview'),
    url(r'inputs/$', input_list_view, name = 'inputs'),
    url(r'inputs/new', input_new_view, name = 'inputnew'),
    url(r'outputs/(?P<output_id>\d+)/$', output_single_view, name = 'output'),
    url(r'outputs/$', output_list_view, name = 'outputs'),
    url(r'apply/(?P<input_id>\d+)/$', apply_view, name='process'),
    url(r'^$', home_view, name='home'),
]
