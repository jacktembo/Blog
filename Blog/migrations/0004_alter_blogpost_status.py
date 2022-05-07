# Generated by Django 4.0.4 on 2022-05-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blogpost_banner_image_alter_blogpost_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1, help_text='This designates the status of this post after saving.'),
        ),
    ]
