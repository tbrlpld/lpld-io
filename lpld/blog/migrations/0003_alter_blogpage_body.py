# Generated by Django 4.1.7 on 2023-04-07 16:39

from django.db import migrations
import wagtail.fields
import wagtailmarkdown.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_add_heading_blocks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("markdown", wagtailmarkdown.blocks.MarkdownBlock())],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]