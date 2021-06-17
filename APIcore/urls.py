from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('rest_auth.urls')),
    path('api/', include('articles.urls')), #This is not good practice, I realized the need for this conflict only at the end of the delivery, sorry.
    path('api/admin/', include('articles.urls')),
    path('api/sign-up/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
]