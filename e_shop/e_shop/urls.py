"""
URL configuration for e_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/',views.master,name='master'),
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

    path('contact_us',views.contact_page,name="contact_page"),

    path('checkout/',views.checkout,name="checkout"),

    path('order/',views.your_order,name="order"),

    path('product/',views.product_page,name="product"),

    path('product/<str:id>',views.product_detail,name='product_detail'),

    path('search/',views.search,name='search'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
