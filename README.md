# Reddit User Persona Generator

This Python-based tool scrapes a Reddit user’s public posts and comments and uses OpenAI’s GPT model to generate a rich user persona. The persona includes interests, personality traits, tone, ideology (if inferable), and supporting citations from the user’s content.

---

## Features

- Scrapes recent Reddit activity (posts + comments)
- Uses OpenAI LLM (GPT-3.5/4) for behavioral analysis
- Outputs a complete persona with cited examples
- Simple CLI-based execution
- Saves results in a local `.txt` file

---

## Technologies Used

- Python 3.10+
- PRAW (Reddit API)
- OpenAI GPT-3.5/4
- python-dotenv

---

## Directory Structure


<img width="354" height="248" alt="image" src="https://github.com/user-attachments/assets/6a57a1c4-d258-41cd-a087-2a854e8bf839" />



---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/aniketjadhav25000/reddit-persona-generator.git
cd reddit-persona-generator
pip install -r requirements.txt
```
### Step 2: Run the Program
```bash
python persona_generator.py --profile https://www.reddit.com/user/kojied/
```
