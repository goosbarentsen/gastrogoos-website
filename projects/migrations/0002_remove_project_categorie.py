# Generated by Django 2.2.7 on 2020-03-19 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categorie',
        ),
    ]