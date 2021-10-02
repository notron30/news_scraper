from django.urls import path
from .views import homepage,ajaxsave,quantumize
app_name = 'blogapp'

urlpatterns = [
    path('homepage/',homepage,name='homepage'),
    path('ajaxsaved/',ajaxsave,name="ajaxsaved"),
    path('quantumize/',quantumize,name="quantumize"),
]
