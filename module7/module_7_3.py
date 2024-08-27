PUNCTUATION = [',', '.', '=', '!', '?', ';', ':', ' - ']

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as file:
                words = []
                for line in file:
                    lower_line = line.lower()
                    non_punc_line = lower_line
                    for char in PUNCTUATION:
                        non_punc_line = non_punc_line.replace(char, '')
                    words = [*words, *non_punc_line.split()]
                all_words[file_name] = words
        return all_words

    def find(self, word):
        words = self.get_all_words().items()
        res = {}
        for n, w in words:
            if word.lower() in w:
                res[n] = w.index(word.lower()) + 1
        return res

    def count(self, word):
        words = self.get_all_words().items()
        res = {}
        for name, words_ in words:
            count = 0
            for w in words_:
                if w == word.lower():
                    count += 1
            res[name] = count
        return res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего