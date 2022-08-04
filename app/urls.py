from django import views
from django.urls import path
from . import views
urlpatterns = [
       path('',views.mytodo,name="mytodo"),
       path('<int:pk>',views.deleteItem,name="deleteItem"),
       path('update/<int:pk>',views.updateItem,name="updateItem")
]
