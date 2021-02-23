# Generated by Django 3.1.5 on 2021-02-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210220_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('matricula', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=128, verbose_name='password')),
            ],
        ),
    ]
