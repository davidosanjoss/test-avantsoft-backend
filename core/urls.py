from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clients.views import TopCustomersStatsView
from sales.views import DailySalesStatsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api/clients/", include("clients.urls")),
    path("api/sales/", include("sales.urls")),
    path("api/statistics/daily-sales/", DailySalesStatsView.as_view(), name="daily-sales"),
    path("api/statistics/top-customers/", TopCustomersStatsView.as_view(), name="top-customers"),
]
