# Generated by Django 5.1.1 on 2024-11-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classPage', '0006_alter_classpages_link_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classpages',
            name='link_page',
        ),
        migrations.AddField(
            model_name='classpages',
            name='url_slug',
            field=models.CharField(default='grammar', max_length=50),
        ),
    ]
