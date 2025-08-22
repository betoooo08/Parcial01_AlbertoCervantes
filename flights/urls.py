from django.urls import path
from .views import HomeView, FlightCreateView, FlightListView, FlightStatsView

app_name = 'flights'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registrar/', FlightCreateView.as_view(), name='create'),
    path('listar/', FlightListView.as_view(), name='list'),
    path('estadisticas/', FlightStatsView.as_view(), name='stats'),
]