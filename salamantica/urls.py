#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static

from salamantica import settings
from cms import urls as cms_urls
from cms import views as cms_views

admin.site.site_header = 'Salamanca Móvil CMS'
admin.autodiscover()


urlpatterns = [

    # Home
    path('', cms_views.home, name='base'),

    # Admin Urls
    path('admin/', admin.site.urls),

    # CMS Urls
    path('cms/', include((cms_urls, 'cms'), namespace='cms')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
