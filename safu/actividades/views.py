from django.shortcuts import render
from django.views import View

from django.views.generic import TemplateView, ListView

from actividades.models import Actividad


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         contexto = {
#             'nombre': 'moises',
#             'actividades': Actividad.objects.all()
#         }
#         return render(request, 'index.html', contexto)

# class HomeView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         return {
#             'nombre': 'moises',
#             'actividades': Actividad.objects.all()
#         }

class HomeView(ListView):
    template_name = 'index.html'
    model = Actividad
    context_object_name = 'actividades'

    def get_context_data(self, **kwargs):
        # contexto = {'actividades': Actividad.objects.all()}
        contexto = super(HomeView, self).get_context_data(**kwargs)
        contexto['nombre'] = 'moises'
        return contexto
