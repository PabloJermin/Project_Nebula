# Generated by Django 5.1 on 2024-09-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_students_quiz_submited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='average_score',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
