
from django.urls import path

from .views import (
    ProductListView, 
    ProductDetailSlugView,
    )
    

urlpatterns = [

    path('',ProductListView.as_view()),
    #path('products-fbv', product_list_view),

    #path('products/<slug:pk>/',ProductDetailView.as_view()),
    path('<slug:slug>/',ProductDetailSlugView.as_view()),
    # path('products-fbv/<slug:slug>/', product_detail_view),

    # path('featured/', ProductFeatureListView.as_view()),
    # path('featured/<slug:pk>/', ProductFeatureDetailView.as_view())
]

