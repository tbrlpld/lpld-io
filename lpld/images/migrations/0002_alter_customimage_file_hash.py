# Generated by Django 4.0.4 on 2022-09-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file_hash",
            field=models.CharField(
                blank=True, db_index=True, editable=False, max_length=40
            ),
        ),
    ]
