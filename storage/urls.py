from django.urls import path
from .views import store_file, get_files

urlpatterns = [
    path('store', store_file, name="store"),
    path('get_files', get_files, name="get"),
]