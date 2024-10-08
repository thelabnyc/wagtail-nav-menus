# Generated by Django 4.1.5 on 2023-01-31 15:10

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_nav_menus", "0003_auto_20191111_1655"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navmenu",
            name="menu",
            field=wagtail.fields.StreamField(
                [
                    (
                        "nav_category",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "sub_nav",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "page_link",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "link",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "django_url",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "url_name",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "relative_url",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "link",
                                                            wagtail.blocks.RegexBlock(
                                                                error_mesage={
                                                                    "invalid": "Not a relative URL"
                                                                },
                                                                regex="^(?!www\\.|(?:http|ftp)s?://|[A-Za-z]:\\\\|//).*",
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(),
                                            ),
                                            ("html", wagtail.blocks.RawHTMLBlock()),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "page_link",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.blocks.BooleanBlock(required=False),
                                ),
                                ("page", wagtail.blocks.PageChooserBlock()),
                            ]
                        ),
                    ),
                    (
                        "external_link",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.blocks.BooleanBlock(required=False),
                                ),
                                ("link", wagtail.blocks.URLBlock()),
                            ]
                        ),
                    ),
                    (
                        "django_url",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.blocks.BooleanBlock(required=False),
                                ),
                                ("url_name", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "relative_url",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.blocks.BooleanBlock(required=False),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.RegexBlock(
                                        error_mesage={"invalid": "Not a relative URL"},
                                        regex="^(?!www\\.|(?:http|ftp)s?://|[A-Za-z]:\\\\|//).*",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    ("html", wagtail.blocks.RawHTMLBlock()),
                ],
                use_json_field=True,
            ),
        ),
    ]
