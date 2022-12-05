from django.urls import path
from . import views

urlpatterns = [
    path('',views.productsView),
    path('<int:id>',views.productDetile),
    path('categories/',views.categoryView),
    path('categories/<str:title>',views.categoryDetile),
]