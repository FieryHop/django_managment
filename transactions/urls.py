from django.urls import path
from transactions import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('create/', views.transaction_create, name='transaction_create'),
    path('<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    path('load-categories/', views.load_categories, name='load_categories'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
]