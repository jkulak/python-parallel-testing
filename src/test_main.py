import unittest
import requests_mock
import main

class TestMain(unittest.TestCase):
    def test_query_api(self):
        with requests_mock.Mocker() as m:
            m.get("https://jsonplaceholder.typicode.com/?query=test", text='api response')
            self.assertEqual(main.query_api("test"), 'api response')

if __name__ == '__main__':
    unittest.main()
