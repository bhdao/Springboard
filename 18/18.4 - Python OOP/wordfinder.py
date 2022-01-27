import random
from sre_constants import CATEGORY

"""Word Finder: finds random words from a dictionary."""

class WordFinder:

    """
    >>> rw = WordFinder("word.txt")
    "Words read:235886"

    >>> rw.random()
    """

    def __init__(self, path):
        self.path = path
        self.words = self.read_file()
        self.word_count()

    def read_file(self):
        return [word[0:len(word)-1] for word in open(self.path,"r")]

    def random(self):
        return self.words[random.randint(0, len(self.words)-1)]

    def word_count(self):
        return f"Words read: {len(self.words)}"


class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)
        self.path = path
        self.words = self.read_file()
        self.words_with_cats = self.set_categories()
        self.words = self.words_with_cats["All Words"]
        self.categories = self.words_with_cats.keys()
        print(f"Total words: {len(self.words)}")
        print(f"Total categories: {len(self.categories)}")

    def set_categories(self):
        cat_dict = {
            "All Words":[]
            }
        current_cat = ""
        for line in self.words:
            # print(line)
            if len(line) > 0 and line[0] == "#":
                current_cat = line[2:len(line)]
                cat_dict[current_cat] = []
            elif line != "":
                cat_dict["All Words"].append(line)
                cat_dict[current_cat].append(line)
        return cat_dict
    
    def random_from_category(self, category):
        return self.words_with_cats[category][random.randint(0, len(self.words_with_cats[category])-1)]
            

        


test = SpecialWordFinder("new_words.txt")
