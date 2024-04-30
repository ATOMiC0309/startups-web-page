from django.urls import path
from .views import index, startup_detail, category_by_types, startups_by_category, page_not_fount

urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:pk>/', startup_detail, name="startup_detail"),
    path('category-by/<int:pk>/', category_by_types, name="category_by_types"),
    path('startup-by/<int:pk>/', startups_by_category, name="startups_by_category"),
    path('page404/', page_not_fount, name="page404")
]
