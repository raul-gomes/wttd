from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Raul Gomes', cpf='12345678900',
                    email='rsgomes86@gmail.com', phone='61-99549-6161')
        self.client.post('/inscricao/', data)
        self.mail = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.mail.subject)

    def test_subscription_email_from(self):

        expect = 'rsgomes86@hotmail.com'

        self.assertEqual(expect, self.mail.from_email)

    def test_subscription_email_to(self):

        expect = ['rsgomes86@hotmail.com', 'rsgomes86@gmail.com']

        self.assertEqual(expect, self.mail.to)

    def test_subscription_email_body(self):
        contents = ['Raul Gomes',
                    '12345678900',
                    'rsgomes86@gmail.com',
                    '61-99549-6161'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.mail.body)