import pytest
import requests_mock
import main

test_data = [
    ("test1", "api response1"),
    ("test2", "api response2"),
    ("beef", "api response for beef"),
    ("chicken", "api response for chicken"),
    ("pork", "api response for pork"),
    ("fish", "api response for fish"),
    ("lamb", "api response for lamb"),
    ("turkey", "api response for turkey"),
    ("duck", "api response for duck"),
    ("veal", "api response for veal"),
    ("salmon", "api response for salmon"),
    ("tuna", "api response for tuna"),
    ("shrimp", "api response for shrimp"),
    ("lobster", "api response for lobster"),
    ("crab", "api response for crab"),
    ("bacon", "api response for bacon"),
    ("ham", "api response for ham"),
    ("sausage", "api response for sausage"),
    ("steak", "api response for steak"),
    ("ribs", "api response for ribs"),
    ("burger", "api response for burger"),
    ("pizza", "api response for pizza"),
    ("pasta", "api response for pasta"),
    ("rice", "api response for rice"),
    ("bread", "api response for bread"),
]

@pytest.mark.parametrize("test_input,expected_output", test_data)
def test_query_api(test_input, expected_output):
    with requests_mock.Mocker() as m:
        m.get(f"https://jsonplaceholder.typicode.com/?query={test_input}", text=expected_output)
        assert main.query_api(test_input) == expected_output
