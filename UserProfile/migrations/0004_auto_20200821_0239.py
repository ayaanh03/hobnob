# Generated by Django 3.1 on 2020-08-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserProfile", "0003_auto_20200821_0206"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="date_of_birth", field=models.DateField(),
        ),
    ]
