# Generated by Django 3.1.7 on 2021-02-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_diet_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
