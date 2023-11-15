import pytest
import requests_mock
import main

test_data = [
    ("test1", "api response1"),
    ("test2", "api response2"),
    # add more test data as needed
]

@pytest.mark.parametrize("test_input,expected_output", test_data)
def test_query_api(test_input, expected_output):
    with requests_mock.Mocker() as m:
        m.get(f"https://jsonplaceholder.typicode.com/?query={test_input}", text=expected_output)
        assert main.query_api(test_input) == expected_output
