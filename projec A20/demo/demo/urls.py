from django.contrib import admin
from django.urls import path, include  # Include is required for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ourapp.urls')),  # Connect the app's URLs to the project
]

