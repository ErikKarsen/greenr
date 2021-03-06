# Generated by Django 3.1.2 on 2021-02-22 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='duration_hours',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
        ),
        migrations.AlterField(
            model_name='journey',
            name='duration_minutes',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)]),
        ),
    ]
