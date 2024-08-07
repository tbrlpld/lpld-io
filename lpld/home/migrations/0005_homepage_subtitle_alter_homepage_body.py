# Generated by Django 4.1.13 on 2024-07-07 23:51

from django.db import migrations, models

import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_homepage_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="subtitle",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.CharBlock(required=True),
                                            )
                                        ]
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "paragraph",
                                                wagtail.blocks.RichTextBlock(
                                                    features=["link", "bold", "italics"]
                                                ),
                                            ),
                                            (
                                                "link_list",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "page_link",
                                                            wagtail.blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "page",
                                                                        wagtail.blocks.PageChooserBlock(
                                                                            required=True
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "text",
                                                                        wagtail.blocks.CharBlock(
                                                                            help_text="Text for the link. Defaults to page title.",
                                                                            required=False,
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ],
                                        min_rum=1,
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
