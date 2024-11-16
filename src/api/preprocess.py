import json
from datetime import datetime

# Function to parse and format timestamps
def format_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

# Function to process user data
def process_user_data(user_data):
    users = []
    for user in user_data["users"]:
        # Formatting user data
        user_info = {
            "id": user["id"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "username": user["username"],
            "email": user["email"],
            "role": user["role"],
            "profile_url": user["profile_url"],
            "bio": user["bio"],
            "website_url": user["website_url"],
            "instagram_url": user["instagram-url"],
            "youtube_url": user["youtube_url"],
            "tiktok_url": user["tictok_url"],
            "is_verified": user["isVerified"],
            "referral_code": user["referral_code"],
            "has_wallet": user["has_wallet"],
            "last_login": format_timestamp(user["last_login"]),
            "share_count": user["share_count"],
            "post_count": user["post_count"],
            "following_count": user["following_count"],
            "follower_count": user["follower_count"],
            "is_online": user["is_online"],
            "location": {"latitude": user["latitude"], "longitude": user["longitude"]}
        }
        users.append(user_info)
    return users

# Function to process liked posts data
def process_liked_posts(liked_posts_data):
    liked_posts = []
    for post in liked_posts_data["posts"]:
        # Formatting liked post data
        post_info = {
            "id": post["id"],
            "title": post["title"],
            "slug": post["slug"],
            "identifier": post["identifier"],
            "category": {
                "id": post["category"]["id"],
                "name": post["category"]["name"],
                "count": post["category"]["count"],
                "description": post["category"]["description"],
                "image_url": post["category"]["image_url"]
            },
            "comment_count": post["comment_count"],
            "upvote_count": post["upvote_count"],
            "view_count": post["view_count"],
            "exit_count": post["exit_count"],
            "rating_count": post["rating_count"],
            "average_rating": post["average_rating"],
            "share_count": post["share_count"],
            "video_link": post["video_link"],
            "thumbnail_url": post["thumbnail_url"],
            "upvoted": post["upvoted"],
            "bookmarked": post["bookmarked"],
            "first_name": post["first_name"],
            "last_name": post["last_name"],
            "username": post["username"],
            "picture_url": post["picture_url"],
        }
        liked_posts.append(post_info)
    return liked_posts

# Function to process viewed posts data
def process_viewed_posts(viewed_posts_data):
    viewed_posts = []
    for post in viewed_posts_data["posts"]:
        # Formatting viewed post data
        post_info = {
            "id": post["id"],
            "title": post["title"],
            "slug": post["slug"],
            "identifier": post["identifier"],
            "category": {
                "id": post["category"]["id"],
                "name": post["category"]["name"],
                "count": post["category"]["count"],
                "description": post["category"]["description"],
                "image_url": post["category"]["image_url"]
            },
            "comment_count": post["comment_count"],
            "upvote_count": post["upvote_count"],
            "view_count": post["view_count"],
            "exit_count": post["exit_count"],
            "rating_count": post["rating_count"],
            "average_rating": post["average_rating"],
            "share_count": post["share_count"],
            "video_link": post["video_link"],
            "thumbnail_url": post["thumbnail_url"],
            "upvoted": post["upvoted"],
            "bookmarked": post["bookmarked"],
            "first_name": post["first_name"],
            "last_name": post["last_name"],
            "username": post["username"],
            "picture_url": post["picture_url"],
        }
        viewed_posts.append(post_info)
    return viewed_posts

# Main function to process all data
def preprocess_data(user_json, liked_posts_json, viewed_posts_json):
    # Load JSON data
    users = process_user_data(user_json)
    liked_posts = process_liked_posts(liked_posts_json)
    viewed_posts = process_viewed_posts(viewed_posts_json)

    # Here you can save or further process the data as needed
    # For example, saving to a database or generating a report
    return {
        "users": users,
        "liked_posts": liked_posts,
        "viewed_posts": viewed_posts
    }

# Example usage with JSON data
if __name__ == "__main__":
    # Load JSON data (replace with actual data in your case)
    with open('data/users.json', 'r') as f:
        user_json = json.load(f)
    with open('data/liked_posts.json', 'r') as f:
        liked_posts_json = json.load(f)
    with open('data/viewed_posts.json', 'r') as f:
        viewed_posts_json = json.load(f)
    
    # Process the data
    processed_data = preprocess_data(user_json, liked_posts_json, viewed_posts_json)

    # Output or further process the result
    print(json.dumps(processed_data, indent=4))
