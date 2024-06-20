import requests

# Step 1: Fetch the ID of the most recent story
new_stories_url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
new_stories_response = requests.get(new_stories_url)
new_stories_ids = new_stories_response.json()

# Step 2: Fetch the details of the most recent story using the ID
most_recent_story_id = new_stories_ids[0]  # Get the ID of the most recent story
story_url = f'https://hacker-news.firebaseio.com/v0/item/{most_recent_story_id}.json'
story_response = requests.get(story_url)
story_data = story_response.json()

# Step 3: Check if the fetched item is a story
if story_data.get('type') == 'story':
    title = story_data.get('title', 'No title')
    author = story_data.get('by', 'Unknown author')
    link = story_data.get('url', 'No link')

    # Step 4: Print out the story details
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Link: {link}")
else:
    print("The most recent item is not a story.")