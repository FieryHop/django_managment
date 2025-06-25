from django.urls import path
from references import views

app_name = 'references'
urlpatterns = [
    path('statuses/', views.status_list, name='status_list'),
    path('statuses/create/', views.status_create, name='status_create'),
    path('statuses/<int:pk>/edit/', views.status_edit, name='status_edit'),
    path('statuses/<int:pk>/delete/', views.status_delete, name='status_delete'),

    # Типы операций
    path('types/', views.type_list, name='type_list'),
    path('types/create/', views.type_create, name='type_create'),
    path('types/<int:pk>/edit/', views.type_edit, name='type_edit'),
    path('types/<int:pk>/delete/', views.type_delete, name='type_delete'),

    # Категории
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Подкатегории
    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/create/', views.subcategory_create, name='subcategory_create'),
    path('subcategories/<int:pk>/edit/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategories/<int:pk>/delete/', views.subcategory_delete, name='subcategory_delete'),

    path('', views.reference_home, name='reference_home'),
]