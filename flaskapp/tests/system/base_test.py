from unittest import TestCase
import flaskapp.app as app


class BaseTest(TestCase):
    def setUp(self):
        app.app.testing = True  # lifetime of this app, we are in testing mode
        self.app = app.app.test_client
