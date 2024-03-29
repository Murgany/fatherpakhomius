# Generated by Django 4.1.7 on 2023-04-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fatherpakhomius', '0015_post_alter_book_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='images', verbose_name='image'),
        ),
    ]
