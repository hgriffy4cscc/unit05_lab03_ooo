"""
For this assignment, you will create a single "Word Count" project.
Your program will present a menu of 4 predefined files (Files are attached below).
The user will select a file, and your program will analyze it.
Your core logic must be encapsulated within a class.

Program Name: Lab10_griffy-1.py
Author: Henry Griffy
The purpose of the program: Generates word counts for a selected file
Starter Code:
    Course Texts:
        Python Crash Course 3rd ed Chapter 10
"""

from pathlib import Path

class MyLib():
    """library of texts"""
    texts: list[MyText] = []

    def __init__(self):
        pass

    def add_text(self, new_text: MyText ):
        """add a text to the library"""
        self.texts.append(new_text)
    

class MyText():
    """class for individual texts"""

    def __init__(self, t_title, t_path):
        self.text_title = t_title
        self.text_path = Path(t_path)

    def get_title(self):
        """return the title for this text"""
        return self.text_title

    def get_path(self):
        """return the path object for this text"""
        return self.text_path
    
    def __repr__(self) -> str:
        print(f"{self.text_title} is at {self.text_path.absolute}")

class Interactions():
    """class to manage user interactions"""
    choice: int

    def __init__(self) -> None:
        self.choice = -1

    def show_menu(self, the_lib):
        """prompt user with menu"""
        print("Please select a file to analyze:")
        for i, t in enumerate(the_lib.texts):
            print(f"{i+1}: {t.get_title()}")
        print(f"{len(the_lib.texts)+1}: Exit")

    def get_text_selection(self, the_lib):
        try:
            self.choice = int(input("Enter your choice:"))-1
        except ValueError:
            print("Please enter one of the numerical options")
            self.show_menu(the_lib)
        self.validate_response(the_lib)

    def validate_response(self, the_lib):
        """method to check if user response is acceptable, re-prompt if not"""
        if self.choice not in range(len(the_lib.texts)+1):
            print("Please choose one of the available texts (or quit)")
            self.show_menu(the_lib)
            self.get_text_selection(the_lib)
    
    def get_choice(self):
        """method to return choice"""
        return self.choice


if __name__ == "__main__":
    texts_in = [
        ("Princess of Mars","texts/princess_mars.txt"),
        ("Tarzan","texts/Tarzan.txt"),
        ("Treasure Island","texts/treasure_island.txt"),
        ("The Count of Monte Cristo","texts/monte_cristo.txt")
        ]
    the_lib = MyLib()
    for t in texts_in:
        the_lib.add_text(MyText(t[0] , t[1]))
    interactions = Interactions()
    interactions.show_menu(the_lib)
    interactions.get_text_selection(the_lib)
    print(interactions.get_choice())

