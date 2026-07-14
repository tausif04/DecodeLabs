#  RuleBot – A Simple Rule-Based Chatbot in Python

RuleBot is a beginner-friendly **rule-based chatbot** built using pure Python. It demonstrates fundamental chatbot concepts using dictionaries, functions, and control flow without relying on machine learning or external libraries.
This project is ideal for students learning Python, basic Natural Language Processing (NLP), or chatbot development.

##  Features
- Interactive command-line chatbot
- Rule-based response system
- Dynamic date and time responses
- Input normalization (case-insensitive)
- Built-in help menu
- Graceful handling of invalid commands
- Handles `Ctrl + C` and `Ctrl + D` safely
- Clean, modular, and well-documented code


## Project Structure
RuleBot/
│
├── chatbot.py          # Main chatbot program
├── README.md           # Project documentation


##  Getting Started

### Prerequisites

Python 3.8 or later

Verify your Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

##  Running the Chatbot

Clone the repository:

```bash
git clone https://github.com/your-username/RuleBot.git
```

Navigate to the project directory:

```bash
cd RuleBot
```

Run the chatbot:

```bash
python chatbot.py
```

or

```bash
python3 chatbot.py
```

---

## Supported Commands

| Command | Description |
|---------|-------------|
| `hello` | Greeting |
| `hi` | Greeting |
| `hey` | Greeting |
| `who are you` | Displays chatbot information |
| `help` | Shows available commands |
| `time` | Displays the current system time |
| `date` | Displays today's date |
| `thanks` | Responds politely |
| `thank you` | Responds politely |
| `bye` | Says goodbye (continues chatting) |
| `exit` | Terminates the chatbot |
| `quit` | Terminates the chatbot |


##  Example Session

```text
==================================================
 Welcome to RuleBot — a simple rule-based chatbot!
 Type 'help' to see available commands.
 Type 'exit' or 'quit' to leave.
==================================================

You: hello
RuleBot: Hello there! How can I help you today?

You: time
RuleBot: The current time is 15:42:18.

You: date
RuleBot: Today's date is Monday, July 13, 2026.

You: help
RuleBot:
Here are the commands I understand:
  hello / hi / hey   - Greet me
  who are you        - Learn about me
  time               - Get the current time
  date               - Get today's date
  thanks             - Say thanks
  bye                - Say goodbye (keeps chatting)
  exit / quit        - Leave the chatbot

You: exit
RuleBot: Thanks for chatting. Goodbye!
``

##  How It Works

The chatbot follows a **rule-based architecture**:

1. User enters a command.
2. Input is normalized by removing whitespace and converting to lowercase.
3. The chatbot checks:
   - Dynamic commands (`time`, `date`)
   - Static predefined responses
4. If no rule matches, a default response is returned.
5. The conversation continues until the user enters `exit` or `quit`.


## 🛠 Technologies Used

- Python 3
- Standard Library
  - `datetime`
  - `sys`
No third-party libraries are required.


## Learning Objectives

This project demonstrates:

- Dictionaries
- Functions
- Modular programming
- Input validation
- Exception handling
- While loops
- Conditional statements
- Command-line interaction
- Rule-based chatbot design

## Future Improvements

- Pattern matching using regular expressions
- Keyword-based conversation
- Conversation history
- Randomized responses
- Weather integration
- Calculator functionality
- Joke and quote commands
- GUI using Tkinter or PyQt
- Voice interaction
- NLP integration using NLTK or spaCy
- AI-powered responses using LLM APIs

