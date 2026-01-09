from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('update/<int:id>/', views.update_expense, name='update_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('export-excel/', views.export_expenses_excel, name='export_excel'),
]