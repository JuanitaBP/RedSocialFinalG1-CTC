# Generated by Django 5.1 on 2024-09-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRS', '0004_rename_usuario_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
