from django.urls import path

from . import views

urlpatterns = [
    path('', views.Clients_LC_View.as_view(), name='clients-list-create'),
    path('<int:id>/', views.Clients_RUD_View.as_view(), name='clients-retrieve-update-delete'),
]
