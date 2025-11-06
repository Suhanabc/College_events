from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_event, name='add_event'),


    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('create/', views.event_create, name='event_create'),
    path('edit/<int:event_id>/', views.event_edit, name='event_edit'),
    path('delete/<int:event_id>/', views.event_delete, name='event_delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('register/<int:event_id>/', views.register_for_event, name='register_event'),
    path('profile/', views.user_profile, name='user_profile'),
]


