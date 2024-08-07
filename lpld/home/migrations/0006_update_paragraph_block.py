# Generated by Django 4.1.13 on 2024-07-12 03:38

from django.db import migrations

import wagtail.blocks
import wagtail.fields

import lpld.core.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_homepage_subtitle_alter_homepage_body"),
    ]

    operations = [
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
                                                lpld.core.blocks.SimpleProseRichtext(),
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
