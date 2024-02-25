# FlashLine_
## A Flashcard Management and Learning Application

#### Video Demo: <https://youtu.be/a0SNT7joNCU>

## Overview

FlashLine_ is a command-line flashcard management and learning application that resembles a physical flashcard learning box. It was created as the final project for CS50's Introduction to Programming with Python by HarvardX.

A flashcard box is a learning tool one might still know from school. They are typically used for memorization and can be an effective aid in language learning and test preparation. In its most basic form, think of a simple box containing a number of small cards. Each card typically shows a question or term on one side and the corresponding answer or definition on the other side. You learn a card by reading the question and trying to recall the answer from memory. Then you check your answer for correctness by having a look at the other side of the card. To help with handling larger flashcard decks, cards are typically categorized by subject/topic. This is usually achieved by using multiple boxes/compartments or marking groups of cards within a single flashcard learning box. More advanced boxes come with compartment dividers that turn them into simple learning systems. A new flashcard usually starts at compartment one and is moved ahead to the next compartment with every correct answer. Incorrect answers move a flashcard back to the first compartment. Like this the learning box provides a simple and efficient way to organize study material and track learning progress.

Some of the key limitations of traditional physical learning boxes are their capacity, accessibility, organization as well as certain difficulties in sharing. A physical box can only hold a limited number of cards and tends to become more and more inconvenient with increasing deck size. You might find yourself carrying multiple heavy boxes with you just to notice that the deck you actually need is inaccessible at home. Also, large decks in physical learning boxes are usually hard to manage/organize. Using multiple boxes with different compartments and color-coded groups of cards might keep you organized for a while but at some point, most boxes will start to suffer from a lack of organization. Sharing your physical box means you will lose access to it and your learning progress most likely needs to be abandoned. You could avoid this issue by sharing a copy of the box/deck, but this again becomes more and more problematic with increasing deck size. Copying a set of potentially hundreds of physical cards is not only a matter of time but also money and contributes to paper waste.

FlashLine_ aims to offer the functionality of a physical flashcard learning box without its key limitations.

## Features

- **Create, Load and Save a Flashcard Box**: Create new flashcard boxes, save and load them to continue learning or share boxes with friends.

- **Learn Flashcards**: Test your knowledge and memorize information by learning flashcards. You can randomly learn all flashcards or focus on cards in a specific category or compartment.

- **Create and Manage Flashcards**: Create and delete categories. Add flashcards to categories, see their details and delete them if needed.

- **Track Progress**: View your learning progress in total or by category. The application will keep track of your progress by moving cards between compartments when learning.

Later I would like to add functionality that allows users to still mark an answer as correct even though this might not match the automatic result. I debated whether to design the learning functionality in a way that requires user input for answering or just confirmation that the recalled answer from memory was correct. The latter offers increased flexibility since question answer pairs can be much more complex. I still decided for requiring the user to input an answer since my primary use for the application will be learning vocabulary and abbreviations for now.

A feature I would like to add in the future is a time stamp for when a card was learned the last time. Based on this I would like to introduce an additional learning mode "LEARN INTERVAL" that lets you review a list of cards based on their current level and a set time till repetition for this level. By doing so the learning frequency for easier cards is reduced and learning is focussed on the more challenging content of the deck. This will allow a user to learn in a more tailored way based on past performance and in the right intervals for long term memorization.

Another feature I would like to add is an "EXPORT" and "IMPORT" functionality that would allow users to easier share the current box. Right now, this is possible as well but requires the user to copy the respective save file from/to the data folder manually. The new functionality would prompt the user for a path to export to or import from.

## How to Use

1. **Create a New Box**:

   - Start the application by running `project.py`.
   - Choose "NEW BOX" from the title menu and give your new flashcard box a name.

2. **Add or Delete Categories and Flashcards**:

   - Select "CREATE & MANAGE" from the main menu.
   - Choose "NEW CATEGORY" to create a new category.
   - Choose "NEW FLASHCARD" to select a category and create new flashcards within.
   - Choose "DELETE CATEGORY" or "DELETE FLASHCARD" to delete unwanted categories/flashcards.
   - Choose "SHOW FLASHCARDS" to see all cards in a category. Select a specific card to show its details.

3. **Learn Flashcards**:

   - Select "LEARN" from the main menu.
   - Choose "LEARN ALL" to practice with all flashcards.
   - Choose "LEARN CATEGORY" to select and learn a specific category.
   - Choose "LEARN LEVEL" to select and learn a specific compartment of the box.
   - Answer the flashcard questions and see the result.

4. **Track Progress**:

   - Select "PROGRESS" from the main menu.
   - Choose "PROGRESS TOTAL" to see an overview of your flashcards by level.
   - Select "BY CATEGORY" to view progress for specific categories.

5. **Save and Load**:

   - Choose "SAVE" from the main menu to save your flashcard box the "data" folder.
   - Choose "LOAD BOX" from the title menu to load an existing flashcard box from the "data" folder.
   - Copy files from or to the "data" folder to share a flashcard box.

6. **Exit the Application**:

   - Exit the application at any time by selecting "EXIT" from the main menu.

## Understanding the Code

### File Structure

The application is divided into three main components: **project.py**, **ui.py**, **box.py**. Additionally, there is a script named **test_project.py** containing test functions, and a folder named **data** for storing flashcard decks as JSON files.

- `project.py`: The entry point and main script for the application.
- `ui.py`: A utility script that provides the user interface, including menus and input validation.
- `box.py`: A script containing classes for creating and managing flashcard boxes and flashcards.
- `test_project.py`: Contains test functions for checking the application's functionality.
- `data/`: The folder where your flashcard boxes are saved as JSON files.

### The `ui.py` Module

The `ui.py` script provides the foundation for the user interface of the application. It defines two classes, called `Menu` and `Selector`, which are used to build the UI. It also provides a base class, called `BaseUI`, with common attributes and methods shared by both `Menu` and `Selector`.

**Functionality:**

1. **Display and Interaction:**
   - The script creates a text-based interface that allows users to interact with the application.
   - It provides a structured display with a title, enumerated options, and a prompt for user input.
   - Users can navigate back and forth through hierarchical menus and select different options to perform certain actions.

2. **Options Handling:**
   - The `Menu` class prints a defined set of menu options, where each option is associated with a specific action or can lead to another menu or selector.
   - The `Selector` class provides a dynamically created list of elements (e.g., all flashcards in a category) the user can choose from. The selected element is then passed to a defined function or another selector.

3. **Input Validation:**
   - The script ensures that user input is validated to prevent invalid selections. It checks for valid option numbers and recognizes special options like "X" for exiting or going back.

**How it Works:**

1. **BaseUI Class:**
   - The `BaseUI` class serves as the parent class for both `Menu` and `Selector`.
   - It contains attributes related to UI elements, such as title, options, the prompt text, and the user's choice.
   - It provides the necessary methods for displaying the UI, like printing the available options (`print_options`) and getting user input (`get_user_input`).
   - It also provides methods for controlling the layout, like clearing the screen (`clear_screen`) and printing lines (`print_line`).
   - The method `display` orchestrates the functionality for use in the `Menu` and `Selector` classes.
   - The main method to run a `Menu` or `Selector` (`run`) must be implemented by subclasses.

2. **Menu Class:**
   - The `Menu` class represents a menu interface with a title and a defined set of options to choose from.
   - It takes a dictionary as argument for `options` with the keys representing the displayed option and the values being the corresponding action.
   - Users can navigate through menu items, and each option leads to an action or to another menu or selector.
   - Users can enter numeric choices to select menu options, and the option "X" for exiting or going back.
   - The main method `run` orchestrates `display` (from the `BaseUI` class), handling and validating user input (`input_validation`) as well as calling or instantiating selected options (`call_or_instantiate`).

3. **Selector Class:**
   - The `Selector` class represents a selection UI with a title and a list of elements to choose from.
   - This class works in conjunction with the `Menu` class and allows users to make specific selections that can be based on dynamic content.
   - It takes a list as argument for `options`. The additional attribute `original_options` is required to enable backwards navigation.
   - Users can select one element from a list, and the selection is subsequently passed on to a function or another `Selector` defined by the argument `instance_or_function`.
   - Users can enter numeric choices to make a selection or the option "X" for going back.
   - The main method `run` orchestrates `display` (from the `BaseUI` class), handling and validating user input (`input_validation`) as well as triggering the final action (`call_or_instantiate`).

In summary, the `ui.py` script provides the essential framework for the application's user interface. It allows users to navigate menus, make selections, and perform actions seamlessly. The scripts use is not limited to FlashLine_ and it could be used in other projects as well. Have a look at the "Instantiation of the UI" part in the `project.py` script as an example of how to use it.

### The `box.py` Module

The `box.py` script is a core part of the application, which enables users to create and manage flashcards. It defines two main classes, called `Box` and `Card` that represent the flashcard learning box with its content.

**Functionality:**

1. **Serialization and Deserialization:**
   - The script provides methods to convert the box and its contents into a dictionary and vice versa.
   - This enables users to save a box to and load a box from a JSON file.

2. **Category and Flashcard Management:**
   - The script includes the necessary methods to add categories and flashcards to or delete them from the box.
   - It allows the adjustment of a flashcard's level based on correct or incorrect answers during learning.

3. **Content Information:**
   - There are methods included to create different lists of categories or flashcards.
   - The script as well makes it possible to count flashcards by level.
   - It as well provides methods for printing the details of a flashcard.

**How it Works:**

1. **Box Class:**
   - The `Box` class represents a flashcard box with a name, a list of `categories`, a list of `levels` and a list of `cards`.
   - Only `name` has to be provided as an argument. The attribute `levels` is predefined.
   - The list of `categories` and `cards` are empty by default and can be manipulated by user input (`add_category`, `delete_category`, `add_card`, `delete_card`).
   - The method `check_category` allows to see if a category with a specific name already exists.
   - A similar function `check_box` is later implemented in `project.py` since it doesn't refer to attributes of the `Box` class.
   - The methods for listing and counting include:
   - Listing the questions of all cards in a specific category (`list_cards_in_category`).
   - Listing all `Card` objects in a specific category (`list_card_obj_in_category`) or level (`list_card_obj_in_level`).
   - Countig all cards in a specific level (`count_cards_level`), optionally taking a list of cards as an argument.
   - Saving a box is done by `save_to_json` that utilizes the modules `os` and `json` as well as the `to_dict` method.
   - Loading a box is achieved by `load_from_json` that as well utilizes the `json` module and the `from_dict` method.

2. **Card Class:**
   - The `Card` class represents individual flashcards with a `question`, an `answer`, a `category`, and a `level`.
   - The attribute `level` is 1 by default and can later be manipulated by the `change_level` method.
   - The attributes `question`, `answer` and `category` need to be provided as arguments at instantiation.
   - The methods `to_dict` and `from_dict` are responsible for de-/serialization and are utilized in the `to_dict` and `from_dict` methods of the `Box` class.
   - Printing the details of a flashcard, including question, answer, and level, can be done by using the `print` method.

In summary, the `box.py` script provides the fundamental functionality for creating, managing, and organizing flashcards in a structured manner. Its methods and attributes are extensively used within the `project.py` script.

### The `project.py` Module

The `project.py` script serves as entry point of the application. It plays a pivotal role by connecting the core functionalities found in `box.py` and `ui.py`, defining the user interface and corresponding functions for selectable options.

**Functionality:**

1. **Utility Functions:**
   - The script includes a set of utility functions to ensure a clean and user-friendly interface.

2. **User Interface Setup:**
   - The script sets up the user interface by creating instances of the `Menu` and `Selector` classes from `ui.py`.
   - It defines the structure of menus and interactions, ensuring that users can easily navigate the application.

3. **Menu and Selector Functions:**
   - The script defines the functions that are called when a menu option is selected.
   - Furthermore it includes a number of supporting functions that perform specific subtasks for the main functionality.

4. **Entry Point:**
   - The script includes the main function as entry point for the application.

**How it Works:**

1. **Utility Functions:**
   - `new_screen` clears the screen (`clear_screen`) and provides some simple layout (`print_line_h`).
   - `clear_screen` clears the screen based on the operating system (Windows/Linux). Mainly acts as a supporting function for `new_screen`.
   - `print_line_h` prints a horizontal line of specified length (default is 20). Mainly acts as a supporting function for `new_screen`
   - `continue_enter` pauses the script and waits for user input. It is mostly used as a supporting function delaying the screen being cleared so users are enabled to read response texts.
   - `clean_input` cleans user input by stripping white space and converting all letters to uppercase.
   - `get_input_yes_no` prompts the user to confirm an action with 'Y' or 'N' and returns cleaned (`clean_input`) and validated (`validate_input_yes_no`) input.
   - `validate_input_yes_no` validates user input by checking if it starts with 'Y' or 'N'. Supporting function for `get_input_yes_no`.
   - `get_input` promts the user for input and returns this input cleaned (`clean_input`) and validated (`validate_input`).
   - `validate_input` uses regular expressions and `re` to ensure input does not include special characters. It also ensures input is not empty. Supporting function for `get_user_input`.

2. **Title Screen Functions:**
   - `display_title_screen` displays the title screen showing the application name as ASCII art (`print_ASCII`) and the name of the author.
   - `print_ASCII` prints a text as ASCII art with the help of `pyfiglet`. Supporting function for `display_title_screen`.

3. **Title Menu Functions:**
   - `new_box_ui` creates a new box, prompting the user for a name (`get_input`) and validating the input (`check_box`). It initiates the main menu by calling `run_main` for the freshly created box. Menu action for "NEW BOX".
   - `check_box` checks if user input matches with the name of existing files in the "save" folder (`list_save_files`). Helper function for `new_box_ui`.
   - `load_box_ui` loads an existing box from a JSON file (`Box.load_from_json`) in the "save" folder (`list_save_files`) utilizing `os` and `json`. Furthermore, it initiates the main menu by calling `run_main` for the loaded box. Menu action for "LOAD BOX".
   - `list_save_files` returns a list of all JSON files in a folder utilizing `os`. Supporting function for `check_box` and `load_box_ui`.

4. **Learn Menu Functions:**
   - `learn_category` provides `learn_cards_ui` with a list of cards in a specific category (`Box.list_card_obj_in_category`). Menu action for "LEARN CATEGORY".
   - `learn_level` passes a list of cards with a specific level (`Box.list_card_obj_in_level`) to `learn_cards_ui`. Menu action for "LEARN LEVEL".
   - `learn_cards_ui` shuffles a given set of flashcards using `random`, initiates learning (`learn_cards`) and prints the overall results of a learning session. Menu action for "LEARN ALL" and supporting function for `learn_category` and `learn_level`.
   - `learn_cards` displays questions, prompts user for answers, cleans (`clean_input`) and handles (`handle_input`) input for a set of cards. Furthermore it prints the learning result for each individual card (`print_result`) and adjusts the cards level accordingly (`card.change_level`). It also keeps track of the learnig results and returns them to `learn_cards` for reporting. Supporting function for `learn_cards_ui`.
   - `handle_input` compares the user's answer with the answer attribute of the flashcard. Helper function for `learn_cards`.
   - `print_result` prints the result of learning a flashcard, including correctness, new level, and the expected answer. Supporting function for `learn_cards`.

5. **Create & Manage Menu Functions:**
   - `new_category_ui()` creates a new category (`Box.add_category`) prompting the user for a name (`get_input`) and validating the input (`Box.check_category`). Menu action for "NEW CATEGORY".
   - `delete_category_ui` deletes a category (`Box.delete_category`) and all associated flashcards. Menu action for "DELETE CATEGORY".
   - `show_card_ui` displays the details of a flashcard (Box.print_card) identified by its question. Menu action for "SHOW FLASHCARDS".
   - `new_card_ui` promts the user for a question and answer (`get_input`) and creates a new flashcard (`Box.add_card`) within a given category. Menu action for "NEW FLASHCARD".
   - `delete_card_ui` deletes a flashcard (`Box.delete_card`) identified by its question. Menu action for "DELETE FLASHCARD".

6. **Progress Menu Functions:**
   - `progress_category_ui` lists all flashcards for a specified category (`Box.list_card_obj_in_category`) and passes them to `progress_ui`. Menu action for "BY CATEGORY".
   - `progress_ui` displays the recent state of the box by counting (`Box.count_cards_level`) and printing the number of flashcards within each level. Menu action defined for "PROGRESS TOTAL" and helper function for `progress_category_ui`.

7. **Save and Exit Functions:**
   - `save_box_ui` it asks for user confirmation (`get_input_yes_no`) and saves the current state of the box to a JSON file (` box.save_to_json`). It defines the menu action for "SAVE" in the main menu.
   - `exit_app_ui` also asks for confirmation (`get_input_yes_no`), then exits the application using `sys`. Menu action for "EXIT".

8. **User Interface Setup:**

   - The `title_menu` and `main_menu` are both set up by creating nested instances of `Menu` and `Selector`.
   - First the `title_menu` is created. There is no instance of `Box` yet.

        - **Structure of the `title_menu`:**
        ```
        Menu
        │
        ├── NEW BOX:
        │   new_box_ui
        │   run_main
        │   │
        │   └── main_menu
        │
        ├── LOAD BOX:
        │   Selector(list_save_files)
        │   load_box_ui
        │   run_main
        │   │
        │   └── main_menu
        │
        └── EXIT:
            exit_app_ui
        ```
   - Selecting `new_box_ui` or `load_box_ui` leads to the instantiation of `box`. Then the `main_menu` is created when the new `box` is passed to the `run_main` function.
   - After navigation to the `main_menu` there is no way back to the `title_menu` besides exiting and restarting the application.
   - The `main_menu` contains several more instances of `Menu` and `Selector` and users can freely navigate back and forth within it.

        - **Structure of the `main_menu`:**
        ```
        Menu
        │
        ├── LEARN:
        │   Menu
        │   │
        │   ├── LEARN ALL:
        │   │   learn_cards_ui
        │   │
        │   ├── LEARN CATEGORY:
        │   │   Selector(box.categories)
        │   │   learn_category
        │   │   learn_cards_ui
        │   │
        │   └── LEARN LEVEL:
        │       Selector(box.levels)
        │       learn_level
        │       learn_cards_ui
        │
        ├── CREATE & MANAGE:
        │   Menu
        │   │
        │   ├── NEW CATEGORY:
        │   │   new_category_ui
        │   │
        │   ├── DELETE CATEGORY:
        │   │   Selector(box.categories)
        │   │   delete_category_ui
        │   │
        │   ├── SHOW FLASHCARDS:
        │   │   Selector(box.categories)
        │   │   Selector(box.list_cards_in_category)
        │   │   show_card_ui
        │   │
        │   ├── NEW FLASHCARD:
        │   │   Selector(box.categories)
        │   │   new_card_ui
        │   │
        │   └── DELETE FLASHCARD:
        │       Selector(box.categories)
        │       Selector(box.list_cards_in_category)
        │       delete_card_ui
        │
        ├── PROGRESS:
        │   Menu
        │   │
        │   ├── PROGRESS TOTAL:
        │   │   progress_ui
        │   │
        │   └── BY CATEGORY:
        │       Selector(box.categories)
        │       progress_category
        │       progress_ui
        │
        ├── SAVE:
        │   save_box_ui
        │
        └── EXIT:
            exit_app_ui
        ```


9. **Entry Point:**

- `main` serves as the entry point of the script displaying the title screen and calling `title_menu.run`. If executed as the main program (`if __name__ == "__main__"`), `main` is called to start the application.

## Dependencies

Flash Line is a command-line application built with `Python 3`. To use it, you need to have Python installed on your system. The application also relies on several Python modules and libraries to provide its functionality. Make sure you have the following dependencies installed:

- **os:** The `os` module is used for handling file operations, including saving/loading a box and clearing the screen.
- **json:** The `json` module is used for saving/loading files to/from JSON.
- **re:** The `re` module is used for matching user input with regex for validation.
- **random:** The `random` module is used for shuffling flashcards for learning.
- **sys:** The `sys` module is used to smoothly exit the application.

 While not strictly required for running the application, I also recommend installing `pyfiglet` in order to correctly display the title screen. You can install pyfiglet using pip.

## Author

FlashLine_ was created by Alexander Kadur as final project for CS50's Introduction to Programming with Python.

## Acknowledgements

I would like to express my thanks and appreciation to the team behind [CS50's Introduction to Programming with Python](https://pll.harvard.edu/course/cs50s-introduction-programming-python) and HarvardX for making high-quality education available to learners worldwide.

Furthermore I want to show gratitude to the authors and contributors of the Python modules and libraries used for creating this application. I am truely grateful for the work of these people and the open-source community for making these tools available.

## License

This application is open-source and distributed under the [MIT License](https://opensource.org/license/mit/).

Copyright 2023 Alexander Kadur

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
