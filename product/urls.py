
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<slug:category_slug>/', views.product_list, name='product-category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product-detail'),
]
