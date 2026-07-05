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

    def __init__(self):
        self.texts: list[MyText] = []

    def add_text(self, new_text: MyText ) -> None:
        """add a text to the library"""
        self.texts.append(new_text)
    
    def get_text(self, index) -> MyText:
        """return a text based on index in list"""
        return self.texts[index]

class MyText():
    """class for individual texts"""

    def __init__(self, t_title, t_path):
        self.text_title = t_title
        self.text_path = Path(t_path)
        self.the_words: dict = {}

    def get_title(self):
        """return the title for this text"""
        return self.text_title

    def get_path(self):
        """return the path object for this text"""
        return self.text_path
    
    def get_contents(self):
        """method to grab contents of a text"""
        return self.text_path.read_text(encoding='utf-8')
    
    def do_word_count(self):
        """method to do the core part of the function"""
        temp_words = self.get_contents().split(" ")
        for w in temp_words:
            if w.strip() in self.the_words:
                self.the_words[w.strip()] += 1
            else:
                self.the_words[w.strip()] = 1
        return len(self.the_words)
    
    def print_report(self):
        """method to output the results of the word count"""
#        max_word_length = max(len(self.the_words.keys()))
        print(f"Trying to print report about {len(self.the_words)} words")
        for w, ct in self.the_words.items():
            print(f"{w} :: {ct}")
    
    def __str__(self):
        return f"{self.text_title} is at {self.text_path.absolute}"

class Interactions():
    """class to manage user interactions"""
    choice: int

    def __init__(self) -> None:
        self.choice = -1

    def __show_menu(self, the_lib):
        """prompt user with menu"""
        print("Please select a file to analyze:")
        for i, t in enumerate(the_lib.texts):
            print(f"{i+1}: {t.get_title()}")
        print(f"{len(the_lib.texts)+1}: Exit")

    def did_user_say_quit(self, the_lib):
        """method to determine which menu option indicates quit (ie, final option)"""
        return self.choice == len(the_lib.texts)

    def get_text_selection(self, the_lib):
        self.__show_menu(the_lib)
        try:
            self.choice = int(input("Enter your choice:"))-1
        except ValueError:
            print("Please enter response in numerical form")
            self.get_text_selection(the_lib)
        if not self.validate_response(the_lib):
            self.choice = -1
            self.get_text_selection(the_lib)

    def validate_response(self, the_lib):
        """method to check if user response is acceptable, re-prompt if not"""
        if self.choice not in range(len(the_lib.texts)+1):
            print("Please choose one of the available options")
            return False
        else:
            return True
    
    def get_choice(self) -> int:
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
    for i, t in enumerate(texts_in):
        text_i = MyText(t[0], t[1])
        the_lib.add_text(text_i)
    interactions = Interactions()
    while not interactions.did_user_say_quit(the_lib):
        interactions.get_text_selection(the_lib)
        if not interactions.did_user_say_quit(the_lib):
            the_lib.get_text(interactions.choice).do_word_count()
            the_lib.get_text(interactions.choice).print_report()
    
    

