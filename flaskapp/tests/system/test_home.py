import flaskapp.tests.system.base_test as basetest
import json


class TestHome(basetest.BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')  # context manager, get request at this endpoint
            self.assertEqual(resp.status_code, 200)
            # convert the response from string to json then assert
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, world!'})