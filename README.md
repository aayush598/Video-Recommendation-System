# Socialverse Data Preprocessing

This project handles the data preprocessing tasks for the Socialverse platform, focusing on processing user data, liked posts, and viewed posts from JSON responses. The script formats timestamps, structures data, and prepares it for further use in analytics, storage, or display. The data preprocessing operations are designed to extract key user information, post details, and interactions like upvotes, views, and comments.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Socialverse Data Preprocessing is a Python-based utility designed to process JSON data from the Socialverse API. It extracts and formats user and post-related information, such as:
- User profile information
- Liked posts data
- Viewed posts data
- Post interactions (comments, upvotes, view counts, etc.)
- Conversion of Unix timestamps to human-readable format

This preprocessed data is ideal for further integration with the Socialverse platform, analytics systems, or storage systems (such as databases or cloud storage).

## Features

- **User Data Processing**: Parses and extracts key user information such as username, bio, last login, location, and other profile details.
- **Liked Posts Data Processing**: Handles posts that users have liked, extracting details such as title, category, video link, and interaction counts.
- **Viewed Posts Data Processing**: Extracts similar details for posts that users have viewed.
- **Timestamp Formatting**: Converts Unix timestamps to a readable date-time format for better understanding and reporting.
- **Data Structuring**: Organizes data in an easy-to-use format, making it ready for further processing or visualization.

## Installation

To set up and use the project locally, follow the steps below:

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/socialverse-data-preprocessing.git
cd socialverse-data-preprocessing
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup
Ensure your JSON data (e.g., users.json, liked_posts.json, viewed_posts.json) is placed in the appropriate directory, or modify the script to load the data from your preferred source.

# Usage
To run the preprocessing script, execute the following command:
```
python src/api/preprocess.py
```
This will process the user data, liked posts, and viewed posts, formatting them and printing the output in a readable format.

## Example Output:
The script will output the processed data as a formatted JSON structure, such as:
```
{
    "users": [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "last_login": "2024-11-16 15:45:30",
            "profile_url": "https://socialverse.com/profile/johndoe",
            "location": {"latitude": 12.3456, "longitude": -76.5432}
        }
    ],
    "liked_posts": [
        {
            "id": 871,
            "title": "Know that the lord he is God Jesus",
            "category": {
                "id": 2,
                "name": "Vible",
                "description": "All the best vibes!",
                "image_url": "https://assets.socialverseapp.com/categories/image.jpg"
            },
            "view_count": 19,
            "video_link": "https://video-cdn.socialverseapp.com/video.mp4",
            "upvote_count": 1,
            "average_rating": 42
        }
    ],
    "viewed_posts": [
        {
            "id": 789,
            "title": "Jesus...is...my...hero",
            "category": {
                "id": 2,
                "name": "Vible",
                "description": "All the best vibes!",
                "image_url": "https://assets.socialverseapp.com/categories/image.jpg"
            },
            "view_count": 20,
            "video_link": "https://video-cdn.socialverseapp.com/video.mp4",
            "upvote_count": 1,
            "average_rating": 44
        }
    ]
}

```

# Directory Structure
```
socialverse-data-preprocessing/
│
├── src/
│   ├── api/
│   │   └── preprocess.py   # Main data processing script
│   ├── data/
│   │   └── users.json      # Example user data
│   ├── requirements.txt    # List of dependencies
│
├── README.md               # Project documentation
└── .gitignore              # Git ignore configuration

```

# Contributing
We welcome contributions! To get started:
- Fork the repository.
- Clone your forked repository.
- Create a new branch for your feature or bugfix.
- Make the necessary changes, ensuring that you follow the project’s coding standards.
- Submit a pull request with a detailed description of your changes.

Please make sure your code passes tests and does not introduce any issues.

## Thank you for using Socialverse Data Preprocessing! We hope this utility helps in making your platform data-ready and efficient for further use.



### Breakdown of Sections:
1. **Project Overview**: Describes the purpose of the project and the problem it solves.
2. **Features**: Lists out the key functionality and what the project offers.
3. **Installation**: Instructions for setting up the project locally.
4. **Usage**: Explains how to run the preprocessing script and gives an example of what the output looks like.
5. **Directory Structure**: Shows the folder structure of the project.
6. **Contributing**: Explains how others can contribute to the project.

This README serves as a comprehensive guide for users to understand, set up, and utilize the data preprocessing functionality of your project. Let me know if you need further adjustments!
