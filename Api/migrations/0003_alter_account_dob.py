# Generated by Django 3.2.15 on 2022-08-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_account_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
    ]
