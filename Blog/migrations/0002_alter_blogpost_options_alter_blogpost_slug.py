# Generated by Django 4.0.4 on 2022-05-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
