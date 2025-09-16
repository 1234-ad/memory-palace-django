from django.urls import path
from . import views

urlpatterns = [
    # Palace URLs
    path('', views.PalaceListView.as_view(), name='palace_list'),
    path('create/', views.PalaceCreateView.as_view(), name='palace_create'),
    path('<uuid:pk>/', views.PalaceDetailView.as_view(), name='palace_detail'),
    path('<uuid:pk>/edit/', views.PalaceUpdateView.as_view(), name='palace_edit'),
    path('<uuid:pk>/delete/', views.PalaceDeleteView.as_view(), name='palace_delete'),
    
    # Room URLs
    path('<uuid:palace_pk>/rooms/create/', views.room_create, name='room_create'),
    path('<uuid:palace_pk>/rooms/<uuid:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    
    # Memory Item URLs
    path('<uuid:palace_pk>/rooms/<uuid:room_pk>/items/create/', views.memory_item_create, name='memory_item_create'),
    path('items/<uuid:item_pk>/toggle-mastery/', views.toggle_mastery, name='toggle_mastery'),
    
    # Study Session URLs
    path('<uuid:palace_pk>/study/', views.start_study_session, name='start_study_session'),
    path('sessions/<uuid:session_pk>/', views.study_session, name='study_session'),
]