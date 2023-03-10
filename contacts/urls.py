from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.contact_info, name='contact_infos')
    path('search/', views.search, name='search')
]
