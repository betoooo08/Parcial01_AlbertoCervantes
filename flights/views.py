from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Avg
from .models import Flight
from .forms import FlightForm

class HomeView(TemplateView):
    template_name = 'flights/index.html'

class FlightCreateView(CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'flights/flight_form.html'
    success_url = reverse_lazy('flights:list')

    def form_valid(self, form):
        messages.success(self.request, "Vuelo registrado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Revisa los campos del formulario.")
        return super().form_invalid(form)

class FlightListView(ListView):
    model = Flight
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'
    ordering = ['price']        # menor precio primero
    paginate_by = 10            # paginación

class FlightStatsView(TemplateView):
    template_name = 'flights/flight_stats.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        total_nac = Flight.objects.filter(type=Flight.FlightType.NATIONAL).count()
        total_int = Flight.objects.filter(type=Flight.FlightType.INTERNATIONAL).count()
        avg_nac   = Flight.objects.filter(type=Flight.FlightType.NATIONAL)\
                                  .aggregate(prom=Avg('price'))['prom']
        ctx.update({'total_nac': total_nac, 'total_int': total_int, 'avg_nac': avg_nac})
        return ctx