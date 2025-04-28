from django.urls import path
from API.views import  inventoryView, seeAPI, nameAPI

urlpatterns = [
    path('item/', seeAPI.as_view()),
    path('item/<str:name1>/', nameAPI.as_view()),
    path('items/', inventoryView.as_view(), name='item-list'),
    path('items/<int:pk>/', inventoryView.as_view(), name='item-detail'),  
]
