import difflib

class SpellChecker2:
    def __init__(self):
        self.known_words = set()  # list of known words

    def add_words(self, words):
        # add new words to the list of known words
        self.known_words.update(words)

    def check_spelling(self, text):
        # tokenize text into words
        words = text.split()
        # check for spelling errors
        spelling_errors = [word for word in words if word not in self.known_words]
        return spelling_errors

    def load_dictionary(self, file_path):
        # read the dictionary file and add its words to the set of known words
        with open(file_path, "r") as file:
            for line in file:
                word = line.strip()
                self.known_words.add(word)

    def clear_known_words(self):
        self.known_words.clear()

    def generate_suggestions(self, word):
        return difflib.get_close_matches(word, self.known_words, n=3, cutoff=0.6)