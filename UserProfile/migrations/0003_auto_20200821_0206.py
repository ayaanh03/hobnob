# Generated by Django 3.1 on 2020-08-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserProfile", "0002_auto_20200821_0153"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateField(default="21.08.2020"),
        ),
    ]
