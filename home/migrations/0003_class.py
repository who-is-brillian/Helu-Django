# Generated by Django 5.1.1 on 2024-11-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_count_class_count_alter_count_mentor_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('sessions', models.IntegerField()),
                ('level', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
    ]