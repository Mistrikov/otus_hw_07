# Generated by Django 5.0 on 2023-12-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_categoryuser_categorycourse_course_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
