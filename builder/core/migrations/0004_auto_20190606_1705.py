# Generated by Django 2.2.2 on 2019-06-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_chunk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chunk',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chunks'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='technologies'),
        ),
    ]
