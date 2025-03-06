from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('new/', views.event_create, name='event_create'),
    path('<int:event_id>/edit/', views.event_update, name='event_update'),
    path('<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('<int:event_id>/update_date/', views.update_event_date, name='update_event_date'),  # ✅ Add this for dragging
    path('register/', views.register, name='register'),
    path('api/', views.event_api, name='event_api'),
]
