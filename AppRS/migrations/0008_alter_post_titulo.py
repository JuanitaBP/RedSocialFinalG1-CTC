# Generated by Django 5.1 on 2024-09-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRS', '0007_alter_post_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
