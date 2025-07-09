from django.urls import path

from . import views

urlpatterns = [
    path('', views.Sales_LC_View.as_view(), name='sales-list-create'),
    path('<int:id>/', views.Sales_RUD_View.as_view(), name='sales-retrieve-update-delete'),
]
