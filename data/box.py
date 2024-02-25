import json
import os

"""
The `box.py` script is a core part of the application, which enables users to create and manage flashcards.
It defines two main classes, called `Box` and `Card`.
"""

# ____________________


class Box:
    """
    Represents a flashcard box with flashcards in different levels and categories.

    Attributes:
        name (str): The name of the box.
        categories (list): A list of all categories for flashcards in the box. Dynamic.
        levels (list): A list of all levels for flashcards in the box. Does not represent difficulty but progress. Static.
        cards (list): A list of all flashcards/instances of Card in the box. Dynamic.
    """

    def __init__(self, name):
        """
        Initializes a new flashcard box.

        Args:
            name (str): The name of the box.
        """
        self.name = name
        self.categories = []
        self.levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.cards = []

    # methods related to saving/loading a box__________

    def to_dict(self):
        """
        Convert the box and its conten to a dictionary. Used for saving the box as JSON.

        Returns:
            dict: A dictionary representing the box.
        """
        return {
            "name": self.name,
            "categories": self.categories,
            "cards": [card.to_dict() for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Box object from a dictionary.

        Args:
            data (dict): A dictionary representing a box.

        Returns:
            Box: A Box object created from the dictionary.
        """
        name = data["name"]
        categories = data["categories"]
        cards = [Card.from_dict(card_data) for card_data in data["cards"]]
        box = cls(name)
        box.categories = categories
        box.cards = cards
        return box

    def save_to_json(self, save_folder="data"):
        """
        Saves the box to a JSON file.

        Args:
            save_folder (str): Folder in root to save the JSON file to. By default 'data'.
        """
        data = self.to_dict()
        file_path = os.path.join(save_folder, f"{self.name}.json")
        with open(file_path, "w") as file:
            json.dump(data, file)

    @classmethod
    def load_from_json(cls, file_path):
        """
        Load a box from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            Box: The Box object loaded from the JSON file.
        """
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls.from_dict(data)

    # methods related to the 'categories' attribute__________

    def check_category(self, category):
        """
        Checks if a category exists in box.categories.

        Args:
            category (str): The category to check.

        Returns:
            bool: True if the category exists, otherwise False.
        """
        if category in self.categories:
            return True
        else:
            return False

    def add_category(self, category):
        """
        Adds a category to box.categories.
        Sorts box.categories alphabetically

        Args:
            category (str): The category to add.
        """
        self.categories.append(category)
        self.categories.sort()

    def delete_category(self, category):
        """
        Deletes a category from box.categories.

        Args:
            category (str): The category to delete.
        """
        self.categories.remove(category)

    # methods related to the 'cards' attribute__________

    def print_card(self, question):
        """
        Prints the details of a flashcard.

        Args:
            question (str): The question of the flashcard.
        """
        for card in self.cards:
            if card.question == question:
                card.print()

    def add_card(self, question, answer, category):
        """
        Creates and adds a new flashcard to box.cards.

        Args:
            question (str): The question for the new flashcard.
            answer (str): The answer to the question.
            category (str): The category for the new flashcard.
        """
        card = Card(question, answer, category)
        self.cards.append(card)

    def delete_card(self, question):
        """
        Deletes a flashcard from box.cards.

        Args:
            question (str): The question of the flashcard.
        """
        for card in self.cards:
            if card.question == question:
                self.cards.remove(card)

    def list_cards_in_category(self, category):
        """
        Lists the questions of all flashcards in a specific category.
        Sorts the list alphabetically.

        Args:
            category (str): The category of the flashcards to list.

        Returns:
            list: List of all Card objects questions in the category.
        """
        cards_in_category = [
            card.question for card in self.cards if card.category == category
        ]
        cards_in_category.sort()
        return cards_in_category

    def list_card_obj_in_category(self, category):
        """
        Lists all Card objects in a specific category.

        Args:
            category (str): The category of the flashcards to list.

        Returns:
            list: List of all Card objects in the category.
        """
        return [card for card in self.cards if card.category == category]

    def list_card_obj_in_level(self, level):
        """
        Lists all Card objects in a specific level.

        Args:
            level (int): The level of the flashcards to list.

        Returns:
            list: List of all Card objects in the level.
        """
        return [card for card in self.cards if card.level == level]

    def count_cards_level(self, list_cards=None):
        """
        Count the number of flashcards in a level of the box.

        Args:
            list_cards (list, optional): List of flashcards to count (defaults to None).

        Returns:
            level_count (dict): A dictionary with levels and counts of flashcards.
        """
        if list_cards is None:
            list_cards = self.cards
        level_count = {level: 0 for level in self.levels}
        for card in list_cards:
            level = card.level
            level_count[level] += 1
        return level_count


# ____________________


class Card:
    """
    Represents a flashcard in a flashcard box.

    Attributes:
        question (str): The question on the flashcard.
        answer (str): The answer to the question.
        category (str): The category to which the flashcard belongs.
        level (int): The level of the box the flashcard is located in.
    """

    def __init__(self, question, answer, category, level=1):
        """
        Initializes a new flashcard.

        Args:
            question (str): The question on the flashcard.
            answer (str): The answer to the question.
            category (str): The category to which the flashcard belongs.
            level (int, optional): The level of the box the flashcard is located in. Default at creation is 1.
        """
        self.question = question
        self.answer = answer
        self.category = category
        self.level = level

    # methods related to saving/loading cards__________

    def to_dict(self):
        """
        Convert the flashcard to a dictionary for saving as JSON.

        Returns:
            dict: A dictionary that represents the Card object.
        """
        return {
            "category": self.category,
            "question": self.question,
            "answer": self.answer,
            "level": self.level,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Card object from a dictionary.

        Args:
            data (dict): A dictionary representing a card.

        Returns:
            Box: A Card object created from the dictionary.
        """
        question = data["question"]
        answer = data["answer"]
        category = data["category"]
        level = data["level"]
        card = cls(question, answer, category, level)
        return card

    # methods related to manipulating cards attributes__________

    def change_level(self, result):
        """
        Changes the level attribute of a Card object.

        Args:
            result (bool): Based on correct or incorrect answers when learning a flashcard.
        """
        if result == True:
            if self.level < 10:
                self.level += 1
        elif result == False:
            self.level = 1

    def print(self):
        """
        prints the details of a flashcard. Includes question, answer and level.
        """
        print(f"QUESTION:\n{self.question}")
        print(f"\nANSWER:\n{self.answer}")
        print(f"\nLEVEL:\n{self.level}")
