from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include( 'gamification.urls' ) ),
    path('django-rq/', include('django_rq.urls')),
]
