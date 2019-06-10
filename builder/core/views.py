from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Project, Technology, Chunk


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_active=True)
        context['technologies'] = Technology.objects.filter(is_active=True, show_at_promo=True)
        context['services'] = Chunk.objects.filter(type=Chunk.SERVICE)
        context['benefits'] = Chunk.objects.filter(type=Chunk.BENEFIT)
        context['team_players'] = Chunk.objects.filter(type=Chunk.TEAM_PLAYER)
        return context
