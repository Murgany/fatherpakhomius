# Generated by Django 3.2.14 on 2022-11-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fatherpakhomius', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Litergie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30)),
                ('time', models.TimeField(null=True)),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
    ]
