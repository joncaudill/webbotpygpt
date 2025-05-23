# QuizBot GPT

A simple Python-based quiz bot using OpenAI's GPT models. This project provides both command-line and web-based interfaces for interactive multiple-choice quizzes.

## Purpose

This project was created as an experiment to try to create a simple web based ChatGPT chat bot.  I created this repository as a personal reference.

## Features

- Interactive quiz sessions powered by GPT-4.1
- Multiple-choice questions with 5 possible answers (a, b, c, d, e)
- Feedback on correct/incorrect answers
- Command-line and web-based (Gradio) interfaces

## Files

- [`quizbot.py`](quizbot.py): Command-line quiz bot that interacts with the user in the terminal.
- [`app_web_based.py`](app_web_based.py): Web-based quiz bot using Gradio for a chat-like interface.
- [`app.py`](app.py): Basic OpenAI chat interface for general prompts.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/joncaudill/quizbot-gpt.git
   cd quizbot-gpt
   ```

2. **Install dependencies:**
   ```sh
   pip install openai gradio
   ```

3. **Set your OpenAI API key:**
   - Obtain your API key from [OpenAI](https://platform.openai.com/).
   - Set the environment variable:
     ```sh
     export OPENAI_TEST_KEY=your_openai_api_key
     ```

## Usage

### Command-Line Quiz Bot

Run the quiz bot in your terminal:
```sh
python quizbot.py
```

### Web-Based Quiz Bot

Launch the Gradio web interface:
```sh
python app_web_based.py
```
Then open the provided local URL in your browser.

### General Chat Interface

For a simple chat with GPT:
```sh
python app.py
```

## License

This repository was created for educational purposes