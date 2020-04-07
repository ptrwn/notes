from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.note_details, name='note_details'),
]