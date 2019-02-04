from django.urls import include, path

from app.api import router

urlpatterns = [
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/', include('rest_auth.urls')),
    path('', include(router.urls)),
]
