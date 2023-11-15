# API_URL = "https://jsonplaceholder.typicode.com/"


def query_api(user_input):
    # response = requests.get(f"{API_URL}?query={user_input}", timeout=5)
    return user_input


print(query_api("test"))
