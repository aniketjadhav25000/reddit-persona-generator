# 🧠 Reddit User Persona Generator

Generate insightful user personas from Reddit profiles using LLM (OpenAI GPT) and Reddit's public data. This tool scrapes a user's posts and comments to build a psychological and behavioral profile with citations.

---

## 🚀 Features

- 🔍 Scrapes recent Reddit posts and comments from any public user
- 🤖 Uses OpenAI's GPT model to generate detailed user personas
- 📄 Outputs results to a text file with source citations
- ⚙️ Command-line interface for easy use

---

## 🛠️ Technologies Used

- Python 3.10+
- [PRAW](https://praw.readthedocs.io/) – Reddit API Wrapper
- OpenAI API (GPT-3.5-Turbo or GPT-4)
- dotenv – For managing environment variables

---

## 📦 Installation

```bash
git clone https://github.com/aniketjadhav25000/reddit-persona-generator.git
cd reddit-persona-generator
pip install -r requirements.txt
