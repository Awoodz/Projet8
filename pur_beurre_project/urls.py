"""pur_beurre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^webapp/', include('webapp.urls')),
    url('admin/', admin.site.urls),
    url(r'^base/', views.base_show),
    url(r'^legalmention/', views.legal_mention),
    url(r'^results/', views.results),
    url(r'^account/', views.account),
    url(r'^product/', views.product),
    url(r'^saved_products/', views.saved_products),
]

import debug_toolbar
urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
