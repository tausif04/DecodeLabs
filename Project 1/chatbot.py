

import datetime
import sys


STATIC_RESPONSES = {
    "hello": "Hello there! How can I help you today?",
    "hi": "Hi! How can I help you today?",
    "hey": "Hey! What can I do for you?",
    "who are you": "I'm a simple rule-based chatbot built in Python.",
    "help": (
        "Here are the commands I understand:\n"
        "  hello / hi / hey   - Greet me\n"
        "  who are you        - Learn about me\n"
        "  time               - Get the current time\n"
        "  date               - Get today's date\n"
        "  thanks             - Say thanks\n"
        "  bye                - Say goodbye (keeps chatting)\n"
        "  exit / quit        - Leave the chatbot"
    ),
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Feel free to come back anytime.",
}

# Commands that should terminate the program.
EXIT_COMMANDS = {"exit", "quit"}

# Default response used when no match is found in either dictionary.
DEFAULT_RESPONSE = "Sorry, I don't understand that command."



def get_current_time() -> str:
    """Return the current time as a formatted string."""
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')}."


def get_current_date() -> str:
    """Return the current date as a formatted string."""
    today = datetime.date.today()
    return f"Today's date is {today.strftime('%A, %B %d, %Y')}."


DYNAMIC_RESPONSES = {
    "time": get_current_time,
    "date": get_current_date,
}


def normalize_input(raw_input: str) -> str:
    return raw_input.lower().strip()


def get_response(user_command: str) -> str:
   
    if user_command in DYNAMIC_RESPONSES:
        handler_function = DYNAMIC_RESPONSES[user_command]
        return handler_function()
    return STATIC_RESPONSES.get(user_command, DEFAULT_RESPONSE)


def is_exit_command(user_command: str) -> bool:
    return user_command in EXIT_COMMANDS


def print_welcome_message() -> None:
    print("=" * 50)
    print(" Welcome to RuleBot — a simple rule-based chatbot!")
    print(" Type 'help' to see available commands.")
    print(" Type 'exit' or 'quit' to leave.")
    print("=" * 50)


def print_farewell_message() -> None:
    
    print("RuleBot: Thanks for chatting. Goodbye!")




def run_chatbot() -> None:
    print_welcome_message()

    while True:
      
        try:
            raw_input_text = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
           
            print()  
            print_farewell_message()
            break

        normalized_command = normalize_input(raw_input_text)

     
        if normalized_command == "":
            print("RuleBot: Please type something. (Try 'help' for options.)")
            continue

      
        if is_exit_command(normalized_command):
         
            print_farewell_message()
            break

        response_text = get_response(normalized_command)

        print(f"RuleBot: {response_text}")


if __name__ == "__main__":
    run_chatbot()
    sys.exit(0)
