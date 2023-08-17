from django.urls import path
from .views import homeview, ictsubjectview
urlpatterns = [
    path('', homeview, name='home'),
    path('ictsubject/', ictsubjectview, name='ictsubject')
]
