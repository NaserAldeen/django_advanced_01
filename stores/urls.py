
from django.urls import path

from . import views
app_name = 'stores'
urlpatterns = [
   
    path('list/', views.store_list, name='list'),

]
