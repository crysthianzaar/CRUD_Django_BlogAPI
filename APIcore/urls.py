from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/', include('rest_auth.urls')),
    path('api/sign-up', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/admin/', include('articles.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]