from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save/', views.save_deposit),
    path('recommend_products_options/', views.recommend_products_options),
    path('recommend_products/', views.recommend_products),
    path('detail/<str:fin_prdt_cd>/', views.deposit_detail),
]