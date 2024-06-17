from django.contrib import admin
from django.urls import path
from .import views
# from .views import login
from .utils import *


urlpatterns = [
    path('',views.home,name="home"),
    path('log_in',views.log_in,name='log_in'),
    path('reg',views.reg,name='reg'),
    path('log_out',views.log_out,name='log_out'),
    path('catagory',views.catagory,name='catagory'),
    path('cart',views.cart,name='cart'),
    # path('get_plot/', views.get_plot, name='get_plot'),
    path('showproduct', views.ShowAllProducts, name='showProducts'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
    path('search/', views.searchBar, name='search'),
    path('product/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('product/<int:pk>/delete-comment', views.delete_comment, name='delete-comment'),


    path('add_category/', views.add_category, name='add_category'),

] 