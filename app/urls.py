from django.urls import include, path
from app.views import home
urlpatterns = [
    path('',home,name="index"),
    
]
