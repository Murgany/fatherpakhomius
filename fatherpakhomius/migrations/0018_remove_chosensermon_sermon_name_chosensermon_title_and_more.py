# Generated by Django 4.1.7 on 2023-04-14 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fatherpakhomius', '0017_alter_post_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chosensermon',
            name='sermon_name',
        ),
        migrations.AddField(
            model_name='chosensermon',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='fatherpakhomius.bookcategory', verbose_name='book category'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sermons', to='fatherpakhomius.sermoncategory', verbose_name='sermon category'),
        ),
    ]