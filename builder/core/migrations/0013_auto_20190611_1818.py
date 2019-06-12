# Generated by Django 2.2.2 on 2019-06-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_project_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunk',
            name='description_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chunk',
            name='description_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chunk',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chunk',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chunk',
            name='special_value_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chunk',
            name='special_value_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name_ru',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
