from django.db import models
from django.template.defaultfilters import slugify


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
    description = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


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

    def __str__(self):
        return f"{self.name}"
