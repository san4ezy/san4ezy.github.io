try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

import os

from PIL import Image
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.template.defaultfilters import slugify
from django.core.files.storage import default_storage as storage


class Technology(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='technologies', blank=True, null=True)
    show_at_promo = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to='portfolio')
    thumbnail = models.ImageField(upload_to='portfolio/thumbs', blank=True, null=True)
    description = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)
    is_active = models.BooleanField(default=True)
    ordering_value = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('ordering_value', 'pk',)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.thumbnail:
            if not self.make_thumbnail():
                raise Exception('Could not create thumbnail - is the file type valid?')
        return super().save(*args, **kwargs)


    def make_thumbnail(self):
        image = Image.open(self.image)
        image.thumbnail(settings.THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True


class Chunk(models.Model):
    SERVICE, BENEFIT, TEAM_PLAYER, CONTACT, SOCIAL_CONTACT, VACANCY = range(6)
    TYPE_CHOICES = (
        (SERVICE, "Service"),
        (BENEFIT, "Benefit"),
        (TEAM_PLAYER, "Team Player"),
        (CONTACT, "Contact"),
        (SOCIAL_CONTACT, "Social Contact"),
        (VACANCY, "Vacancy"),
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    special_value = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='chunks', blank=True, null=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    ordering_value = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('ordering_value', 'pk',)

    def __str__(self):
        return f"{self.name}"


class Page(models.Model):
    name = models.CharField(max_length=64)
    template = models.CharField(max_length=255)
    language = models.CharField(max_length=8, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    def __str__(self):
        return f"{self.name}"
