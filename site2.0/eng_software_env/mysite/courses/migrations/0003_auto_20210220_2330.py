# Generated by Django 3.1.5 on 2021-02-20 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210131_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='edicap',
            new_name='edicao',
        ),
    ]
