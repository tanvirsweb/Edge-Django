from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('',views.home, name='home'),
    # http://127.0.0.1:8000/newpage/
    path('newpage',views.newpageh, name='newpageh'),
    # http://127.0.0.1:8000/page01/
    path('page1',views.page1, name='page1'),
]