import requests_mock
import main

def test_query_api():
    with requests_mock.Mocker() as m:
        m.get("https://jsonplaceholder.typicode.com/?query=test", text='api response')
        assert main.query_api("test") == 'api response'
