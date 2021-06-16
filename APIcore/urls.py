from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('rest_auth.urls')),
    path('api/sign-up/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/admin/', include('articles.urls')),
]