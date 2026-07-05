"""
For this assignment, you will create a single "Word Count" project. Your program will present a menu of 4 predefined files (Files are attached below). The user will select a file, and your program will analyze it. Your core logic must be encapsulated within a class.

Program Name: Lab10_griffy-1.py
Author: Henry Griffy
The purpose of the program: Generates word counts for a selected file
Starter Code:
    Course Texts:
        Python Crash Course 3rd ed Chapter 10
"""

from pathlib import Path

class MyLib():
    texts: list[MyText] = []

    def __init__(self):
        pass

    def add_new_text(self, *new_text: MyText ):
        self.texts.append(new_text)
    
class MyText():
    text_title: str = ""
    text_path: Path = None

    def __init__(self, t_title, t_path):
        self.text_title = t_title
        self.text_path = Path(t_path)


if __name__ == "__main__":
    texts_in = [
        ("Princess of Mars","texts/princess_mars.txt"),
        ("Tarzan","texts/Tarzan.txt"),
        ("Treasure Island","texts/treasure_island.txt"),
        ("The Count of Monte Cristo","texts/monte_cristo.txt")
        ]
    the_lib = MyLib()
    for t in texts_in:
        the_lib.add_new_text(t[0], t[1])
    print(len(the_lib.texts))


