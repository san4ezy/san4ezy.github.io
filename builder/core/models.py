from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='technologies', blank=True, null=True)
    show_at_promo = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    image = models.ImageField(upload_to='portfolio')
    description = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Chunk(models.Model):
    SERVICE, BENEFIT, TEAM_PLAYER = range(3)
    TYPE_CHOICES = (
        (SERVICE, "Service"),
        (BENEFIT, "Benefit"),
        (TEAM_PLAYER, "Team Player"),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='chunks', blank=True, null=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    ordered_value = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('ordered_value', 'pk',)

    def __str__(self):
        return f"{self.name}"


class Page(models.Model):
    name = models.CharField(max_length=64)
    template = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
