from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='Index'),
    path('add/',views.add,name='Add'),
    path('edit/update/<int:pk>/',views.update,name='Update'),
    path('edit/<int:pk>/',views.edit,name='Edit'),
    path('delete/<int:pk>/',views.delete_item,name='Delete'),
    path('filter/',views.filter,name="Filter")
]