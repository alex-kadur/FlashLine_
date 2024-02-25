import os

"""
The `ui.py` script provides the foundation for the user interface of the application.
It defines two classes, called `Menu` and `Selector`, which are used to build the UI.
It also provides a base class, called `BaseUI`, with common attributes and methods shared by both `Menu` and `Selector`.
"""
# ____________________


class BaseUI:
    """
    Base class for user interfaces. Used as parent class for Menu and Selector.

    Attributes:
        title (str): Title of the UI. Printed top left.
        options (dict or list): Dictionary of menu options and corresponding actions or list of options. Printed as enumerated list.
        prompt_text (str): Text prompt for user input.
        choice (str): User's choice for selection.
    """

    def __init__(self, title, options):
        """
        Initializes a BaseUI instance.

        Args:
            title (str): The title of the user interface.
            options (dict or list): Dictionary of menu options and corresponding actions or list of options.
        """
        self.title = title
        self.options = options
        self.prompt_text = "YOUR CHOICE: "
        self.choice = None

    def display(self):
        """
        Clears screen, displays the title, options and prompts for user input.
        """
        self.clear_screen()
        self.print_line()
        print(f"{self.title}\n")
        self.print_options()
        self.get_user_input()

    def get_user_input(self):
        """
        Gets user input for selection.
        """
        self.choice = input(f"\n{self.prompt_text}")

    def clear_screen(self):
        """
        Clears the screen based on operating system, uses os module.
        """
        if os.name == "posix":
            os.system("clear")
        else:
            pass

    def print_line(self):
        """
        Prints a line. For layout purposes.
        """
        print("\n", 20 * "_", "\n")

    def print_options(self):
        """
        Enumerates and prints the options, replacing enumeration with "X" for options "EXIT" or "BACK"
        """
        if isinstance(self.options, dict):
            for i, (key, value) in enumerate(self.options.items(), start=1):
                if key == "EXIT" or key == "BACK":
                    print(f"  X: {key}")
                else:
                    print(f"  {i}: {key}")
        if isinstance(self.options, list):
            options_copy = self.options.copy()
            options_copy.append("BACK")
            for i, option in enumerate(options_copy, start=1):
                if option == "BACK":
                    print(f"  X: {option}")
                else:
                    print(f"  {i}: {option}")

    def run(self):
        """
        The main method to run the menu or selector. Subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement the run method.")


# ____________________


class Menu(BaseUI):
    """
    Class representing a menu with title and a set of options. Inherits from BaseUI.

    Attributes:
        title (str): Title of the menu.
        options (dict): Dictionary of menu options, keys are option names, values are either functions or instances of Menu or Selector.
    """

    def run(self, parent_menu=None):
        """
        Run the menu user interface. Navigate through the menu options based on user's choice and executes selecte actions.

        Args:
            parent_menu (instance): A reference to the parent menu, if any. Needed for navigation.
        """
        while True:
            self.display()
            if self.input_validation():
                if self.choice.upper() == "X":
                    if "BACK" == list(self.options.keys())[-1]:
                        break
                    else:
                        selected_option = list(self.options.values())[-1]
                        self.call_or_instantiate(selected_option)
                else:
                    index = int(self.choice) - 1
                    selected_option = list(self.options.values())[index]
                    self.call_or_instantiate(selected_option)
            else:
                print("\nINVALID CHOICE - ENTER A VALID OPTION OR 'X'")
                input("\nPRESS 'ENTER' TO CONTINUE")
                pass

    def call_or_instantiate(self, selected_option=None):
        """
        Calls or instantiates the selected option.

        Args:
            selected_option (function or instance): Selected option, which can be a function, submenu or a selector.
        """
        if callable(selected_option):
            selected_option()
        elif isinstance(selected_option, Menu):
            selected_option.run(self)
        elif isinstance(selected_option, Selector):
            selected_option.run()

    def input_validation(self):
        """
        Checks if the user input is valid (either 'X' or one of the option numbers provided by print_options).

        Returns:
            bool: True if choice is valid, otherwise False.
        """
        if self.choice.upper() == "X":
            return True
        elif self.choice.isdigit() and 1 <= int(self.choice) <= len(self.options) - 1:
            return True
        else:
            return False


# ____________________


class Selector(BaseUI):
    """
    Class representing a selection UI with title and a set of options. Inherits from BaseUI.

    Attributes:
        title (str): Title of the selector.
        original_options: Reference to the original options passed when creating the Selector. Needed for navigation.
        instance_or_function: Function or instance to call and pass the selection to.
    """

    def __init__(self, title, options, instance_or_function):
        """
        Initialize the Selector instance.

        Args:
            title (str): Title of the selector.
            options (list or function): List of options the user can choose from or function to call if there is a parent_selector/selection.
            instance_or_function(instance or function): Function or instance to call and pass selction to.
        """
        super().__init__(title, options)
        self.title = f"AVAILABLE {title}:"
        self.original_options = options
        self.instance_or_function = instance_or_function

    def run(self, parent_selector=None, parent_selection=None):
        """
        Run the selector user interface. Display a list of options and pass the selection to a defined function or instance.

        Args:
            parent_selector (instance): A reference to the parent selector, if any. Needed for navigation.
            parent_selection (str): A reference to the parents selection, if any. Needed for navigation.
        """

        while True:
            if not self.options:
                print(f"\nNOTHING HERE - TRY SOMETHING ELSE")
                input(f"\nPRESS 'ENTER' TO CONTINUE")
                break
            else:
                if parent_selection:
                    self.options = self.original_options(parent_selection)
                self.display()
                if self.input_validation():
                    if self.choice.upper() == "X":
                        break
                    else:
                        self.call_or_instantiate()
                else:
                    print(f"\nINVALID CHOICE - PLEASE ENTER A VALID OPTION OR 'X'")
                    input(f"\nPRESS 'ENTER' TO CONTINUE")
                    pass

    def call_or_instantiate(self):
        """
        Calls or instantiates the selected option.

        """
        index = int(self.choice) - 1
        selected_option = self.options[index]

        if callable(self.instance_or_function):
            self.instance_or_function(selected_option)
        elif isinstance(self.instance_or_function, Selector):
            self.instance_or_function.run(self, selected_option)
        else:
            print(f"\nDEFINED FUNCTION NOT CALLABLE")

    def input_validation(self):
        """
        Checks if the user input is valid (either 'X' or a option number provided by print_options).

        Returns:
            bool: True if input is valid, otherwise False.
        """
        if self.choice.upper() == "X":
            return True
        elif self.choice.isdigit() and 1 <= int(self.choice) <= len(self.options):
            return True
        else:
            return False
