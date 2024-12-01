"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from products.views import (ProductListView,
                            ProductDetailView,
                            ProductDetailSlugView,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView)
from .views import home_page, about_page, contact_page, login_page, register_page

from .views import home_page, about_page, contact_page, login_page, logout_page, register_page

from .views import home_page, about_page, contact_page, login_page, logout_page, register_page, clear_logout_message, servico_1, servico_2, servico_3, servico_4, servico_5

from . import views


urlpatterns = [
	path('', home_page),
	path('about/', about_page),
	path('contact/', contact_page),
    path('login/', login_page),
    path('logout/', logout_page),
    path('mudarsenha/', views.mudar_senha, name='mudar_senha'),
    path('clear-logout-message/', clear_logout_message, name='clear_logout_message'),
    path('register/', register_page),
    #path('featured/', ProductFeaturedListView.as_view()),# chega a dar raiva de tao inutil
    #path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),# chega a dar raiva de tao inutil
    #path('products/', ProductListView.as_view()),
    #path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/2', servico_1),
    path('products/3', servico_2),
    path('products/4', servico_3),
    path('products/5', servico_4),
    path('products/6', servico_5),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
	path('admin/', admin.site.urls),
    path('formularios/', views.mostrar_formulario, name='mostrar_formulario'),
    path('sucesso/', views.formulario_sucesso, name='formulario_sucesso'),
    
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)