import time

import requests

API_URL = "https://jsonplaceholder.typicode.com/"


def query_api(user_input):
    response = requests.get(f"{API_URL}?query={user_input}", timeout=5)

    # sleep for 2 seconds
    time.sleep(2)

    return "just a test"


print(query_api("test"))
