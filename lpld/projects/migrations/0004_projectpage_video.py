# Generated by Django 4.0.4 on 2022-06-07 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mediafiles", "0001_initial"),
        ("projects", "0003_alter_projectpage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectpage",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mediafiles.custommedia",
            ),
        ),
    ]
