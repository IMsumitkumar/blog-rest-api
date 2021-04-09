
from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListView.as_view()),
    path('blogs-details/<int:pk>/', BlogDetailView.as_view()),
    # path('blogging/', BlogView.as_view())
]
