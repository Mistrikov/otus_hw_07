# Generated by Django 5.0 on 2023-12-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_course_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='Описание курса', max_length=1024),
        ),
    ]
