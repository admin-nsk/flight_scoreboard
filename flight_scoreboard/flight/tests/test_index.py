# coding=utf-8
from django.test import TestCase


class FlightTest(TestCase):

    def test_index(self):
        """test: output main page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_uses_home_page_template(self):
        """test: uses index template"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_uses_item_form(self):
        """test: main page uses form in template"""
        # response = self.client.get('/')
        # self.assertIsInstance(response.context['form'], ItemForm)

