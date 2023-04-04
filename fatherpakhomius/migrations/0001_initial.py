# Generated by Django 3.2.14 on 2022-10-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SermonCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio')),
                ('video', models.FileField(blank=True, null=True, upload_to='video')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fatherpakhomius.sermoncategory')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('book', models.FileField(null=True, upload_to='books')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fatherpakhomius.bookcategory')),
            ],
        ),
    ]
