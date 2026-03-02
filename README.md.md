# Telegram Feedback Bot (python-telegram-bot version)

A simple bot that forwards user messages to an admin and stores them in a SQLite database.

## Features
- Forwards any text message to a predefined admin chat.
- Saves messages with user details (ID, username, full name) in SQLite.
- Replies with a thank‑you message.
- Rate limiting to prevent spam.
- Logging for debugging.

## Requirements
- Python 3.8+ (any stable version, no Rust needed)
- A Telegram bot token (from [@BotFather](https://t.me/BotFather))
- Your Telegram chat ID (from [@userinfobot](https://t.me/userinfobot))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-feedback-bot.git
   cd telegram-feedback-bot