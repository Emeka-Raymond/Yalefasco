from django.urls import path

from .import views
urlpatterns = [
    # Category urls
    path('category/', views.CategoryView.as_view()),
    path('category/<int:id>/', views.CategoryDetailView.as_view()),

    # Collections urls
    path('collection/', views.CollectionView.as_view()),
    path('collection/<int:id>/', views.CollectionDetailView.as_view()),

    # PRODUCTS urls
    path('product/', views.ProductView.as_view()),
    path('product/<int:id>/', views.ProductDetailView.as_view()),

]