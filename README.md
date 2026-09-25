# 🧠 LeetTracker

A Telegram-based **LeetCode progress tracker** that helps you follow a structured roadmap, receive daily problems, and verify your progress directly through LeetCode.

LeetTracker connects a Telegram bot, a FastAPI backend, a SQLite database, and the LeetCode GraphQL API into one workflow.

---

## ✨ Features

### 🗺️ Roadmap Mode

Choose a structured LeetCode roadmap and work through problems in order.

Currently supported:

* NeetCode 75
* NeetCode 150

Each user has their own roadmap position, which is updated as they complete problems.

### 🔔 Reminder Mode

Register your LeetCode username and use LeetTracker primarily for reminders.

### 📅 Daily Problems

Roadmap users receive their next problem automatically every day at:

**09:00 Africa/Addis_Ababa**

### ✅ LeetCode Verification

When a user finishes a problem, they can press:

> ✅ I've solved it

The bot checks the user's recent accepted LeetCode submissions and verifies whether the problem was solved.

If verified, the user's roadmap position is advanced automatically.

### 👤 User Profiles

The backend stores:

* Telegram ID
* LeetCode username
* Selected mode
* Selected roadmap
* Current roadmap position

### 🔙 Setup Navigation

The setup flow supports:

* Back
* Cancel
* Roadmap selection
* Mode selection

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**

### Telegram Bot

* **python-telegram-bot**
* **JobQueue** for scheduled daily problems

### External API

* **LeetCode GraphQL API**

### HTTP Client

* **HTTPX**

### Data

* CSV-based roadmap/problem seed data

---


## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd leetcode-tracker-bot
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

For the Telegram JobQueue:

```bash
pip install "python-telegram-bot[job-queue]"
```

### 4. Configure the bot

Create your configuration with your Telegram bot token.

Example:

```python
BOT_TOKEN = "your-telegram-bot-token"
```

Do **not** commit your bot token to GitHub.

---

## 🗄️ Database

The project currently uses SQLite:

```text
leetcode_tracker.db
```

## 🚀 Running the Application

The project has two processes.

### Start FastAPI

From the project root:

```bash
python -m uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

### Start the Telegram Bot

In another terminal:

```bash
python -m bot.bot
```

You should see:

```text
Bot is running...
Daily problems scheduled for 09:00 Africa/Addis_Ababa
```

---

## 🔌 API Endpoints

### Create User

```http
POST /users
```

Creates a new LeetTracker user.

### Get All Users

```http
GET /users
```

Returns registered users.

### Get User

```http
GET /users/{telegram_id}
```

Returns a specific user.

### Update Roadmap Position

```http
PUT /users/{telegram_id}/position
```

Updates the user's current roadmap position.

---

## 🧠 LeetCode Integration

LeetTracker communicates with LeetCode's GraphQL endpoint to retrieve:

* User profile information
* Recent accepted submissions
* Problem slugs
* Submission timestamps

## 🔐 Current Limitations

This project is currently under active development.

Some planned improvements include:

* LeetCode username validation during registration
* Better API error handling
* More complete NeetCode 75/150 datasets
* PostgreSQL support for production
* Authentication and authorization improvements
* Deployment
* Better handling of historical submissions
* Automated tests
* Docker support
* Improved reminder functionality
* User progress statistics
* More detailed profile information

---

## 🎯 Project Goal

LeetTracker is designed to turn LeetCode practice from a collection of solved problems into a **structured, trackable routine**.

Instead of manually remembering:

> "Which problem am I supposed to solve today?"

LeetTracker handles the bookkeeping and lets the user focus on solving the problem.
