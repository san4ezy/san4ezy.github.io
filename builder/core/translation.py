from modeltranslation.translator import register, TranslationOptions

from core.models import Project, Chunk


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Chunk)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'special_value',)
