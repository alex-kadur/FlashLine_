import os
import re
import random
import sys

from ui import Menu
from ui import Selector
import box

try:
    import pyfiglet
    pyfiglet_installed = True
except ImportError:
    pyfiglet_installed = False

"""
The `project.py` script serves as entry point of the application.
It plays a pivotal role by connecting the core functionalities found in `box.py` and `ui.py`.
It definines the user interface and the corresponding functions for selectable options.
"""

# ______Utility functions______
# for common tasks throughout the application


def new_screen():
    """
    Clears the screen and prints a line.
    """
    clear_screen()
    print_line_h()


def clear_screen():
    """
    Clears the screen based on the operating system (Windows/Linux).
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def print_line_h(lenght=20):
    """
    Prints a horizontal line.

    Args:
        lenght (int, optional): The lenght of the line (defaults to 20).
    """
    print()
    print(lenght * "_")
    print()


def continue_enter():
    """
    Pauses the execution of the script and waits for random user input to continue.
    """
    input("\nPRESS 'ENTER' TO CONTINUE")
    pass


def clean_input(user_input):  # test
    """
    Clean user input by stripping and converting to uppercase.

    Args:
        user_input (str): The input provided by the user.

    Returns:
        str: Cleaned user input.
    """
    cleaned_input = user_input.strip().upper()
    return cleaned_input


def get_input_yes_no(action):
    """
    Prompts the user to confirm an action with 'Y' or 'N' and returns validated input.

    Args:
        action (str): The action to confirm. Used only for the prompt.

    Returns:
        bool: True if user input starts with 'Y'. False if user input starts with 'N'.

    """
    while True:
        new_screen()
        user_input = clean_input(input(f"\nDO YOU REALLY WANT TO {action}? (Y/N): "))
        if validate_input_yes_no(user_input) == False:
            print(f"\nINVALID INPUT - TYPE 'Y' OR 'N'")
            continue_enter()
        else:
            if user_input.startswith("Y"):
                return True
            else:
                return False


def validate_input_yes_no(user_input):  # test
    """
    Validates user input by checking if it starts with 'Y' or 'N' (case-insensitive).

    Args:
        user_input (str): The user's input.

    Returns:
        bool: True if user input starts with 'Y' or 'N'. False if not.
    """
    if user_input.startswith("Y") or user_input.startswith("N"):
        return True
    else:
        return False


def get_input(prompt, object, disable_validation=True):
    """
    Gets user input with a specified prompt.

    Args:
        prompt (str): The first part of the prompt.
        object (str): Second part of the prompt. The name of the object to interact with.

    Returns:
        str: user_input
    """
    prompt_complete = f"{prompt} {object}: "
    while True:
        new_screen()
        user_input = clean_input(input(prompt_complete))
        if disable_validation == True:
            return user_input
        else:
            if validate_input_general(user_input) == True:
                return user_input
            else:
                print(f"\nINVALID INPUT - MAKE SURE NOT TO USE SPECIAL CHARACTERS")
                continue_enter()


def validate_input_general(user_input):  # test
    """
    Validates user input by ckecking input is not empty and there are no special characters.

    Args:
        user_input (str): The user's input.

    Returns:
        bool: True, if input is valid. Otherwise False.
    """
    pattern = r"^[a-zA-Z0-9_-]+$"
    if re.match(pattern, user_input) and user_input != "":
        return True
    else:
        return False


# ______Functions related to the TITLE screen______
# display the applications title screen


def display_title_screen():
    """
    Displays the title screen with application name and author.
    """
    new_screen()
    if pyfiglet_installed:
        print_ASCII("FLASH")
        print_ASCII("  LINE_")
    else:
        print(f"FLASH")
        print(f"\nLINE_")
        print(f"\n(INSTALL PYFIGLET TO CORRECTLY DISPLAY THE TITLE)")
    print(20 * "_")
    print(f"\nFLASHCARD LEARNING AND MANAGEMENT")
    continue_enter()


def print_ASCII(text, font="slant"):
    """
    Prints a text as ASCII art using a specified font.

    Args:
        text (str): The text to display as ASCII art.
        font (str, optional): The font for creating the ASCII art. Defaults to 'slant'.
    """
    ascii_text = pyfiglet.figlet_format(text, font=font)
    print(ascii_text)


# ______Functions related to the TITLE Menu__________
# define actions that can be selected from the title menu


def new_box_ui():
    """
    Menu action for "NEW BOX".
    Creates a new flashcard box and starts the main menu.
    """
    global box
    name = get_input(f"NAME OF NEW", "BOX", disable_validation=False)
    if check_box(name) == False:
        box = box.Box(name)
        print(f"\nBOX '{name}' CREATED")
        continue_enter()
        run_main(box)
    elif check_box(name) == True:
        print(f"\nBOX WITH NAME '{name}' ALREADY EXISTS - CHOOSE A DIFFERENT NAME")
        continue_enter()


def check_box(name):
    """
    Checks if a flashcard box with the given name already exists.

    Args:
        name (str): Name to check for.

    Returns:
        bool: True, if a box with the given name exists. Otherwise False.
    """
    if name in list_save_files("data"):
        return True
    else:
        return False


def load_box_ui(filename, save_folder="data"):
    """
    Menu action for "LOAD BOX". Load an existing flashcard box from a JSON file and start the main menu.

    Args:
        filename (str): The name of the box to load (without file extension).
        save_folder (str, optional): The subfolder in root where the JSON file is saved. Defaults to 'data'.
    """
    global box
    file_path = os.path.join(save_folder, f"{filename}.json")
    try:
        box = box.Box.load_from_json(file_path)
        print(f"\nBOX '{filename}' LOADED")
        continue_enter()
        run_main(box)
    except FileNotFoundError:
        print(f"\nCOULD NOT LOAD BOX '{filename}' - MAKE SURE THE FILE EXISTS")
        continue_enter()


def list_save_files(save_folder="data"):
    """
    Returns a list of all JSON files in a folder without the file extension.
    Uses os.path to get the folder of the script.

    Args:
        save_folder (str, optional): Name of the folder with JSON save-files. Assumed to be subfolder of root. By default "data".

    Returns:
        list: List of all file names (box names) without file extensions.
    """
    list_json_files_folder = []
    script_path = os.path.dirname(os.path.realpath(__file__))
    save_folder_path = os.path.join(script_path, save_folder)

    for filename in os.listdir(save_folder_path):
        file_path = os.path.join(save_folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".json"):
            name, _ = os.path.splitext(filename)
            list_json_files_folder.append(name)
    return list_json_files_folder


# ______functions related to the LEARN Menu______
# allow users to learn all flashcards or cards in a specific category or level


def learn_category(category):
    """
    Menu action for "LEARN CATEGORY".
    Starts learn_cards_ui for flashcards in a specific category.

    Args:
        category (str): The category to learn flashcards from.
    """
    cards = box.list_card_obj_in_category(category)
    learn_cards_ui(cards)


def learn_level(level):
    """
    Menu action for "LEARN LEVEL".
    Starts learn_cards_ui for flashcards in a specific level.

    Args:
        level (int): The level to learn flashcards from.
    """
    cards = box.list_card_obj_in_level(level)
    learn_cards_ui(cards)


def learn_cards_ui(cards=None):
    """
    Menu action for "LEARN ALL" (if cards is default).
    Shuffles cards and calls learn_cards for a given set of flashcards (or all flashcards if default).

    Args:
        cards (list, optional): The list of flashcards to learn. Defaults to None.
    """
    if cards == None:
        cards = box.cards
    if cards == []:
        print("\nNO CARDS HERE")
        continue_enter()
    else:
        random.shuffle(cards)
        count_all, count_correct = learn_cards(cards)
        new_screen()
        print(f"{count_correct} OUT OF {count_all} ANSWERS CORRECT")
        continue_enter()


def learn_cards(cards):
    """
    For a set of flashcards, prints question, prompts user for answer.
    Passes answer to handle_input to check correctnes (result).
    Passes result to print_result to inform user.
    Counts and returns learned cards and correct answers.

    Args:
        cards (list): The list of flashcards to learn.

    Returns:
        tuple: The total number of questions and the number of correct answers.
    """
    count_all = 0
    count_correct = 0
    for card in cards:
        new_screen()
        print(f"QUESTION: {card.question}")
        answer = clean_input(input(f"\nYOUR ANSWER (OR 'X' TO GO BACK): "))
        if answer == "X":
            break
        else:
            result = handle_input(card, answer)
            count_all += 1
            if result == True:
                count_correct += 1
            card.change_level(result)
            print_result(card, result)
            continue_enter()
    return (count_all, count_correct)


def handle_input(card, answer):
    """
    Compares the user's answer with the answer attribute of the learned flashcard.

    Args:
        card (Card): The flashcard being answered.
        answer (str): The user's answer.

    Returns:
        bool: True if the answer is correct. Otherwise False.
    """
    if answer == card.answer:
        return True
    else:
        return False


def print_result(card, result):
    """
    Prints the result of learning a flashcard, including correctness, new level and the expected answer.

    Args:
        card (Card): The flashcard being answered.
        result (bool): True if the answer was correct. Otherwise False.
    """
    if result == True:
        if (card.level - 1) < 10:
            print(f"\nCORRECT - CARD MOVED TO LEVEL {card.level}")
        else:
            print(f"\nCORRECT")

    elif result == False:
        print(f"\nWRONG - CARD MOVED TO LEVEL 1")
        print(f"\nCORRECT ANSWER: {card.answer}")


# ______functions related to the CREATE & MANAGE Menu______
# allow users to create and delete categories and flashcards
# allow users to see all flashcards in a category and the details of individual flashcards


def new_category_ui():
    """
    Menu action for "NEW CATEGORY".
    Creates a new category for flashcards.
    """
    new_screen()
    while True:
        name = get_input("ENTER NAME OF NEW", "CATEGORY")
        if box.check_category(name) == False:
            box.add_category(name)
            print(f"\nCATEGORY '{name}' CREATED")
            continue_enter()
            break
        elif box.check_category(name) == True:
            print(
                f"\nCATEGORY WITH NAME '{name}' ALREADY EXISTS - CHOOSE A DIFFERENT NAME"
            )
            continue_enter()


def delete_category_ui(category):
    """
    Menu action for "DELETE CATEGORY".
    Deletes a category and all associated flashcards.

    Args:
        category (str): The category to be deleted.
    """
    new_screen()
    box.delete_category(category)
    for card in box.cards:
        if card.category == category:
            box.cards.remove(card)
    print(f"CATEGORY '{category} DELETED")
    continue_enter()


def show_card_ui(card_question):
    """
    Menu action for "SHOW FLASHCARDS".
    Displays the details of a flashcard identified by its question.

    Args:
        card_question (str): The question of an existing flashcard.
    """
    new_screen()
    box.print_card(card_question)
    continue_enter()


def new_card_ui(category):
    """
    Menu action for "NEW FLASHCARD".
    Creates a new flashcard within a given category.

    Args:
        category (str): The category the flashcard is associated with.
    """
    question = get_input("ENTER", "QUESTION")
    answer = get_input("ENTER", "ANSWER")
    new_screen()
    box.add_card(question, answer, category)
    print(f"\nNEW FLASHCARD '{question}' CREATED")
    continue_enter()


def delete_card_ui(card_question):
    """
    Menu action for "DELETE FLASHCARD".
    Deletes a flashcard identified by its question.

    Args:
        card_question (str): The question of an existing flashcard.
    """
    new_screen()
    box.delete_card(card_question)
    print(f"\nFLASHCARD DELETED")
    continue_enter()


# ______functions related to the PROGRESS Menu______
# allow users to track progress for the whole box or a specific category


def progress_ui(list_cards=None):
    """
    Menu action for "PROGRESS TOTAL".
    Displays the recent state of the box by listing the number of flashcards within each level.
    If no specific list provided, shows result for all flashcards (box.cards).

    Args:
        list_cards (list, optional): List of flashcards to consider. Defaults to None.
    """
    if list_cards is None:
        list_cards = box.cards
    new_screen()
    cards_per_level = box.count_cards_level(list_cards)
    print("FLASHCARDS PER LEVEL:\n")
    for level, count in cards_per_level.items():
        formatted_level = f"{level:02}"
        print(f"LEVEL {formatted_level}: {count}")
    input("\nPRESS 'ENTER' TO GO BACK")


def progress_category(category):
    """
    Menu action for "BY CATEGORY".
    Lists all flashcards for a specified category and passes list to progress_ui.

    Args:
        The category to list and pass flashcards for.
    """
    cards_in_category = box.list_card_obj_in_category(category)
    progress_ui(cards_in_category)


# ______functions related to SAVE and EXIT______
# allow users to save the current flashcard box and progress
# allow users to exit the application


def save_box_ui():
    """
    Menu action for "SAVE".
    Saves the current state of the box to a JSON file.
    """
    while True:
        if get_input_yes_no("SAVE") == True:
            save_folder = "data"
            box.save_to_json(save_folder)
            print(f"\nBOX {box.name} SAVED")
            continue_enter()
            break
        else:
            print(f"\nBOX NOT SAVED")
            continue_enter()
            break


def exit_app_ui():
    """
    Menu action for "EXIT".
    Exits the application after asking user for confirmation.
    """
    while True:
        new_screen()
        if get_input_yes_no("QUIT") == True:
            print(f"\nTHANK YOU FOR USING 'FLASH LINE_' - COME BACK SOON")
            print_line_h()
            print(f"\n© 2023 ALEXANDER KADUR")
            continue_enter()
            clear_screen()
            sys.exit()
        else:
            break


# ______UI Setup______
# structures the application and allows users to navigate the application
# links menu options to specific actions to be performed on selection


title_menu = Menu(
    "WELCOME - WHAT DO YOU WANT TO DO?",
    {
        "NEW BOX": new_box_ui,
        "LOAD BOX": Selector("BOXES", list_save_files(), load_box_ui),
        "EXIT": exit_app_ui,
    },
)


def run_main(box):
    main_menu = Menu(
        "MAIN MENU:",
        {
            "LEARN": Menu(
                "MAIN MENU > LEARN:",
                {
                    "LEARN ALL": learn_cards_ui,
                    "LEARN CATEGORY": Selector(
                        "CATEGORIES", box.categories, learn_category
                    ),
                    "LEARN LEVEL": Selector("LEVELS", box.levels, learn_level),
                    "BACK": None,
                },
            ),
            "CREATE & MANAGE": Menu(
                "MAIN MENU > CREATE & MANAGE:",
                {
                    "NEW CATEGORY": new_category_ui,
                    "DELETE CATEGORY": Selector(
                        "CATEGORIES", box.categories, delete_category_ui
                    ),
                    "SHOW FLASHCARDS": Selector(
                        "CATEGORIES",
                        box.categories,
                        Selector(
                            "FLASHCARDS", box.list_cards_in_category, show_card_ui
                        ),
                    ),
                    "NEW FLASHCARD": Selector(
                        "CATEGORIES", box.categories, new_card_ui
                    ),
                    "DELETE FLASHCARD": Selector(
                        "CATEGORIES",
                        box.categories,
                        Selector(
                            "FLASHCARDS", box.list_cards_in_category, delete_card_ui
                        ),
                    ),
                    "BACK": None,
                },
            ),
            "PROGRESS": Menu(
                "MAIN MENU > PROGRESS:",
                {
                    "PROGRESS TOTAL": progress_ui,
                    "BY CATEGORY": Selector(
                        "CATEGORIES", box.categories, progress_category
                    ),
                    "BACK": None,
                },
            ),
            "SAVE": save_box_ui,
            "EXIT": exit_app_ui,
        },
    )

    main_menu.run()


# ______Entry point______
# is excuted as the main program when 'project.py' is run
# displays the title screen and initiates the title menu


def main():
    display_title_screen()
    title_menu.run()


if __name__ == "__main__":
    main()
