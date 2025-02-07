# master/urls.py
from django.urls import path, include
from .views import serve_static_page

urlpatterns = [
    path('live/', include(('master.dummy_app.live', 'live'), namespace='live')),

    path('<str:filename>', serve_static_page, name='serve_static_page'),
]
