# Generated by Django 4.1.7 on 2023-04-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fatherpakhomius', '0013_alter_sermon_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='book',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='booksbyotherfather',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='chosensermon',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='chosensermon',
            name='speaker',
            field=models.CharField(blank=True, max_length=100, verbose_name='speaker'),
        ),
        migrations.AddField(
            model_name='sermon',
            name='speaker',
            field=models.CharField(blank=True, max_length=100, verbose_name='speaker'),
        ),
        migrations.AddField(
            model_name='sermoncategory',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='sermonsbyotherfather',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='sermonsbyotherfather',
            name='speaker',
            field=models.CharField(blank=True, max_length=100, verbose_name='speaker'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date_created'),
        ),
    ]