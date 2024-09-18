# Generated by Django 5.1 on 2024-09-18 03:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRS', '0008_alter_post_titulo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='seguidores',
            field=models.ManyToManyField(blank=True, related_name='seguidores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='seguidos',
            field=models.ManyToManyField(blank=True, related_name='seguidos', to=settings.AUTH_USER_MODEL),
        ),
    ]
