# Generated by Django 3.2.15 on 2022-10-09 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='prdt',
            new_name='prodt',
        ),
    ]
