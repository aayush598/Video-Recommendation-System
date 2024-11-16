import requests
import json

BASE_URL = "https://api.socialverseapp.com"
HEADERS = {
    "Flic-Token": "flic_b9c73e760ec8eae0b7468e7916e8a50a8a60ea7e862c32be44927f5a5ca69867"
}

def fetch_data(endpoint, save_path):
    """Fetch data from an API and save it to a JSON file."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        with open(save_path, 'w') as file:
            json.dump(response.json(), file)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Fetch all data
fetch_data("/posts/view?page=1&page_size=1000", "data/viewed_posts.json")
fetch_data("/posts/like?page=1&page_size=5", "data/liked_posts.json")
fetch_data("/posts/rating?page=1&page_size=5", "data/ratings.json")
fetch_data("/posts/summary/get?page=1&page_size=1000", "data/posts.json")
fetch_data("/users/get_all?page=1&page_size=1000", "data/users.json")