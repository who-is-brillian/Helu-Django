# Generated by Django 5.1.1 on 2024-12-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
