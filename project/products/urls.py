from django.urls import path
from .views import ProductListView ,CategoryListView



urlpatterns = [
    path('product/',ProductListView.as_view()),
    path('category/',CategoryListView.as_view()),
]

