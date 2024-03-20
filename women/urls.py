from django.urls import path
from .views import WomenListApiView

urlpatterns = [
    path('all/', WomenListApiView.as_view())
]