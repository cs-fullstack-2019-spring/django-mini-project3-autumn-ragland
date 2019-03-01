from django.urls import path
from . import views

urlpatterns = [
    # read
    path('', views.index, name='index'),
    # add
    path('add/', views.add, name='add'),
    # read
    path('listTeacher/<int:id>', views.listTeacher, name='listTeacher'),
    path('listSchool/<int:id>', views.listSchool, name='listSchool'),
    # update
    path('edit/<int:id>', views.edit, name='edit'),
    # delete
    path('delete/<int:id>', views.delete, name='delete'),
]
