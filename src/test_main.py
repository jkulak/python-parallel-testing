import unittest
import requests_mock
import main
from concurrent.futures import ThreadPoolExecutor

class TestMain(unittest.TestCase):
    def test_query_api(self, test_input, expected_output):
        with requests_mock.Mocker() as m:
            m.get(f"https://jsonplaceholder.typicode.com/?query={test_input}", text=expected_output)
            self.assertEqual(main.query_api(test_input), expected_output)

if __name__ == '__main__':
    test_data = [
        ("test1", "api response1"),
        ("test2", "api response2"),
        # add more test data as needed
    ]

    with ThreadPoolExecutor() as executor:
        for test_input, expected_output in test_data:
            executor.submit(unittest.main().test_query_api(test_input, expected_output))
