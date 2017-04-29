from django.views.generic import TemplateView, ListView

from actividades.models import Actividad


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(HomeView, self).get_context_data(**kwargs)
        contexto['actividades'] = Actividad.objects.all().order_by('-fecha')[:3]
        return contexto


class ActividadesView(ListView):
    template_name = 'actividades.html'
    model = Actividad
    context_object_name = 'actividades'
