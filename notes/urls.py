from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from notes.views import user_views, notes_views

urlpatterns = [
    path('login/', obtain_auth_token , name='login'),
    path('register/', user_views.user_create , name='register' ),
    path('users/me/', user_views.user_me , name='me'),
    path('users/', user_views.users_list , name='users'),
    path('users/is_unique/<str:username>/', user_views.user_is_unique , name='users_is_unique'),
    path('users/<str:pk>/', user_views.user_id , name='user_detail'),
    path('notes/', notes_views.notes , name='notes'),
    path('notes/<str:pk>/', notes_views.note_details , name='note_details'),
    
   
]
