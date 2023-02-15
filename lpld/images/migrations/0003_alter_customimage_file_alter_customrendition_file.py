# Generated by Django 4.0.9 on 2023-02-15 01:28

from django.db import migrations

import wagtail.images.models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0002_alter_customimage_file_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file",
            field=wagtail.images.models.WagtailImageField(
                height_field="height",
                upload_to=wagtail.images.models.get_upload_to,
                verbose_name="file",
                width_field="width",
            ),
        ),
        migrations.AlterField(
            model_name="customrendition",
            name="file",
            field=wagtail.images.models.WagtailImageField(
                height_field="height",
                upload_to=wagtail.images.models.get_rendition_upload_to,
                width_field="width",
            ),
        ),
    ]
