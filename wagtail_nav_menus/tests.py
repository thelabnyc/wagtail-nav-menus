from django.test import TestCase
from .models import NavMenu
import json


class NavMenuTestCase(TestCase):
    def setUp(self):
        self.json_menu = [
            {'type': 'external_link', 'value': {'open_in_new_tab': True,
                                                'link': 'http://www.google.com', 'override_title': 'TITLE'}},
            {'type': 'page_link', 'value': {
                'open_in_new_tab': False, 'page': 2, 'override_title': ''}},
            {'type': 'image', 'value': 1},
            {'type': 'html', 'value': '<div> html is here </div>'},
            {'type': 'nav_category', 'value': {'title': 'a nav cat', 'sub_nav': [
                {'type': 'page_link', 'value': {
                    'open_in_new_tab': False, 'page': 1, 'override_title': ''}},
            ]}},
        ]

    def test_menu_json(self):
        """ Test serializing and deserializing the menu json """
        menu = NavMenu.objects.create(
            name="top",
            menu=json.dumps(self.json_menu)
        )

        output_json = menu.to_json()
        output = json.loads(output_json)

        self.assertEqual(output[0]['type'], "external_link")
        self.assertEqual(output[0]['value']['link'], "http://www.google.com")

    def test_render_menu(self):
        json_menu = json.dumps(self.json_menu)
        NavMenu.objects.create(name="top", menu=json_menu)
        NavMenu.objects.create(name="bottom", menu=json_menu)
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
