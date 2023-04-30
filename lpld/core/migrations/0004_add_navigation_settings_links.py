# Generated by Django 4.1.7 on 2023-04-30 06:40

import django.db.models.deletion
from django.db import migrations, models

import modelcluster.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        ("core", "0003_delete_technology"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrimaryNavigation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PrimaryNavigationLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("text_override", models.CharField(blank=True, max_length=65)),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "setting",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="core.primarynavigation",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
