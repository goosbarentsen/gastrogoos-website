# Generated by Django 2.2.7 on 2020-03-24 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='afbeelding',
        ),
    ]
