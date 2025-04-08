from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home route
    path('festival/<int:festival_id>/', views.festival_detail, name='festival_detail'),  # Festival details route
    path('archive/', views.archive, name='archive'),  # Archive route
    path('add/', views.add_entry, name='add_entry'),  # Add entry route (note the trailing slash)
    path('about/', views.about, name='about'),    # About Page
    path('login/', views.login_view, name='login'),  # Login Page
    path('signup/', views.signup, name='signup'),
    path('', views.calendar_view, name='home'),  # Homepage routing
]
