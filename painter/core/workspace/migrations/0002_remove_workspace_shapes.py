# Generated by Django 4.1 on 2022-08-14 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='shapes',
        ),
    ]
