from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('auth/', include('api.root.auth.urls', namespace='auth'))
]