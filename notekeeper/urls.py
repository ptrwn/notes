from django.urls import path
from . import views

app_name = 'notekeeper'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.note_details, name='note_details'),
    path('new/', views.create_note, name='create_note'),
    path('delete/', views.delete_note, name='delete_note'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('<uuid:note_uuid>', views.publish_note, name='publish_note')
]
