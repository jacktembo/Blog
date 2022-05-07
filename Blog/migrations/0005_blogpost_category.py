# Generated by Django 4.0.4 on 2022-05-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_blogpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('python', 'Python'), ('kotlin', 'Kotlin'), ('javascript', 'Javascript'), ('html-css', 'HTML/CSS'), ('hacking', 'Ethical Hacking'), ('devops', 'DevOps'), ('django', 'Django'), ('reactjs', 'React JS'), ('other', 'Other')], default='python', max_length=255),
            preserve_default=False,
        ),
    ]
