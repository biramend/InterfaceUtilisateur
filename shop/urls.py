from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('show/<str:slug>/', views.show, name="show"),
    path('show/<str:slug>/add_to_cart/', views.add_to_cart, name="cart"),
    path('panier/', views.panier, name="panier"),
    path('panier/delete', views.panier_delete, name="panier_delete"),
]