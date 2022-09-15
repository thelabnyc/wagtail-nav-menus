# Generated by Django 2.2.5 on 2019-09-11 17:45

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_nav_menus.models


def set_default_site(apps, schema_editor):
    Site = apps.get_model("wagtailcore", "Site")
    NavMenu = apps.get_model("wagtail_nav_menus", "NavMenu")
    site = Site.objects.filter(is_default_site=True).first()
    if site:
        for menu in NavMenu.objects.all():
            menu.site = site
            menu.save()


def do_nothing(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0040_page_draft_title"),
        ("wagtail_nav_menus", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="navmenu",
            options={
                "verbose_name": "Navigation Menu",
                "verbose_name_plural": "Navigation Menus",
            },
        ),
        migrations.AddField(
            model_name="navmenu",
            name="site",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wagtailcore.Site",
            ),
        ),
        migrations.RunPython(set_default_site, do_nothing),
        migrations.AlterField(
            model_name="navmenu",
            name="site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wagtailcore.Site"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="navmenu",
            name="menu",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "nav_category",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("title", wagtail.core.blocks.CharBlock()),
                                (
                                    "sub_nav",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "page_link",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.core.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.core.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.core.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.core.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "link",
                                                            wagtail.core.blocks.URLBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "django_url",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.core.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.core.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "url_name",
                                                            wagtail.core.blocks.CharBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "relative_url",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "override_title",
                                                            wagtail.core.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "open_in_new_tab",
                                                            wagtail.core.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "link",
                                                            wagtail.core.blocks.RegexBlock(
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
                                            (
                                                "html",
                                                wagtail.core.blocks.RawHTMLBlock(),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "page_link",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.core.blocks.BooleanBlock(required=False),
                                ),
                                ("page", wagtail.core.blocks.PageChooserBlock()),
                            ]
                        ),
                    ),
                    (
                        "external_link",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.core.blocks.BooleanBlock(required=False),
                                ),
                                ("link", wagtail.core.blocks.URLBlock()),
                            ]
                        ),
                    ),
                    (
                        "django_url",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.core.blocks.BooleanBlock(required=False),
                                ),
                                ("url_name", wagtail.core.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "relative_url",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "override_title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "open_in_new_tab",
                                    wagtail.core.blocks.BooleanBlock(required=False),
                                ),
                                (
                                    "link",
                                    wagtail.core.blocks.RegexBlock(
                                        error_mesage={"invalid": "Not a relative URL"},
                                        regex="^(?!www\\.|(?:http|ftp)s?://|[A-Za-z]:\\\\|//).*",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    ("html", wagtail.core.blocks.RawHTMLBlock()),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="navmenu",
            name="name",
            field=models.CharField(
                choices=[("top", "Top"), ("footer", "Footer")], max_length=50
            ),
        ),
        migrations.AlterUniqueTogether(
            name="navmenu",
            unique_together={("site", "name")},
        ),
    ]
