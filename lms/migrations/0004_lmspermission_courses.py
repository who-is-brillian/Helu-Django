# Generated by Django 5.1.3 on 2024-12-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_lmspermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='lmspermission',
            name='courses',
            field=models.ManyToManyField(blank=True, to='lms.course'),
        ),
    ]