# Generated by Django 5.1 on 2024-09-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_students_cohort'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_attended',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
