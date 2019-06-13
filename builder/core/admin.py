import requests

from django.contrib import admin

from core.models import Technology, Project, Chunk, Page
from django.template.loader import render_to_string

from core.views import IndexView
from django.urls import reverse


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_at_promo', 'is_active',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'is_active',)


@admin.register(Chunk)
class ChunkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'special_value', 'type', 'ordering_value',)
    list_filter = ('type',)
    list_editable = ('ordering_value',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    actions = ('build',)

    def build(self, request, queryset):
        for obj in queryset:
            # response = render_to_string(obj.template, {})
            response = requests.get(
                f"http://localhost:8000{reverse(obj.template)}",
                headers={'Accept-Language': obj.language}
            )
            with open(f'../{obj.name}.html', 'w') as static_file:
                static_file.write(response.content.decode())
