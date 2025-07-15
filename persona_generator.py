import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
import praw

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username(profile_url: str) -> str:
    """Extracts the username from a Reddit profile URL."""
    return profile_url.rstrip("/").split("/")[-1]

def fetch_reddit_data(username: str) -> dict:
    """Fetches posts and comments for a given Reddit user."""
    print(f"[INFO] Collecting activity for u/{username}...")

    try:
        redditor = reddit.redditor(username)
        posts = [f"{post.title} - {post.selftext}" for post in redditor.submissions.new(limit=20)]
        comments = [comment.body for comment in redditor.comments.new(limit=20)]
    except Exception as e:
        print(f"[ERROR] Failed to fetch data for {username}: {e}")
        posts, comments = [], []

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }

def analyze_user_behavior(data: dict) -> str:
    """Uses OpenAI to generate a user persona from Reddit activity."""
    prompt = f"""
You are a behavior analyst. Based on the following Reddit posts and comments, create a user persona.

Include the following:
- Interests
- Personality traits
- Estimated age range
- Political/social leanings (if identifiable)
- Writing style
- Other behavioral traits

Include short citations (summarized) from posts/comments that support each point.

--- Posts ---
{data['posts']}

--- Comments ---
{data['comments']}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are analyzing a Reddit user's digital behavior."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] OpenAI failed: {e}")
        return "Persona generation failed."

def save_persona_to_file(username: str, persona_text: str):
    """Saves the generated persona to a local file."""
    os.makedirs("data", exist_ok=True)
    output_path = os.path.join("data", f"{username}_persona.txt")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(persona_text)

    print(f"[SUCCESS] Persona saved at: {output_path}")

def run(profile_url: str):
    username = extract_username(profile_url)
    user_content = fetch_reddit_data(username)

    if not user_content["posts"] and not user_content["comments"]:
        print("[INFO] No content found for this user.")
        return

    persona = analyze_user_behavior(user_content)
    save_persona_to_file(username, persona)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a user persona from Reddit profile activity.")
    parser.add_argument("--profile", required=True, help="Full Reddit user profile URL (e.g., https://www.reddit.com/user/exampleuser)")
    args = parser.parse_args()

    run(args.profile)
