from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('',views.home, name='home'),
    path('index/', views.home, name='index'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('why/',views.why, name='why'),
    path('team/',views.team, name='team'),
    # http://127.0.0.1:8000/newpage/
    path('newpage',views.newpageh, name='newpageh'),
]