# Generated by Django 5.1.3 on 2024-12-15 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_lmspermission_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lmspermission',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='lmspermission', to='lms.course'),
        ),
    ]
