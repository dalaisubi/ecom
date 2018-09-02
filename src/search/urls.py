
from django.urls import path

from products.views import (
    ProductListView, 
    )
from .views import SearchProductView
    
app_name = 'search'
urlpatterns = [

    path('',SearchProductView.as_view(), name='list'),
]

