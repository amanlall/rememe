# Generated by Django 3.0.2 on 2020-05-06 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comments_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
