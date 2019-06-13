# Generated by Django 2.2.2 on 2019-06-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chunk',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Service'), (1, 'Benefit'), (2, 'Team Player'), (3, 'Contact'), (4, 'Social Contact'), (5, 'Vacancy')]),
        ),
    ]