# Generated by Django 3.0.2 on 2020-05-01 05:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200430_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='memer',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
