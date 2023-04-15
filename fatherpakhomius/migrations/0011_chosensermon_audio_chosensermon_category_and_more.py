# Generated by Django 4.1.7 on 2023-04-07 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fatherpakhomius', '0010_alter_chosensermon_sermon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chosensermon',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio', verbose_name='sermon audio'),
        ),
        migrations.AddField(
            model_name='chosensermon',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fatherpakhomius.sermoncategory', verbose_name='sermon category'),
        ),
        migrations.AlterField(
            model_name='chosensermon',
            name='sermon_name',
            field=models.CharField(max_length=200, verbose_name='sermon name'),
        ),
    ]