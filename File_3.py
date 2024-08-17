import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding="utf-8") as file:
                spisok = []
                for line in file:
                    line = line.lower()
                    marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for x in line:
                        if x in marks:
                            line = line.replace(x, "")
                    d = line.split()
                    spisok += d
                all_words[i] = spisok
        return all_words


    def find(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                return {name: words.index(word)+1}

    def count(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                return {name: words.count(word)}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего