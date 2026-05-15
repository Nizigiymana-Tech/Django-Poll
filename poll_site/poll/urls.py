from django.urls import path
from . import views

urlpatterns = [
    path('poll/<int:pk>/', views.post_detail, name="poll_detail"),
    path('', views.poll, name='poll')
]