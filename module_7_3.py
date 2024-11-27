class WordsFinder:
    def __init__(self, *file_txt):
        self.file_txt = file_txt
    def get_all_words(self):
        all_words = {}
        for keys in self.file_txt:
            with open(keys, 'r', encoding='utf-8') as file:
                values = []
                for line in file:
                    line = line.lower()
                    sings = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in sings:
                        line = line.replace(symbol, '' if symbol != ' - ' else ' ')
                    values.extend(line.split())
                all_words[keys] = values
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for keys, values in self.get_all_words().items():
            if word in values:
                result[keys] = values.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for keys, values in self.get_all_words().items():
            result[keys] = values.count(word)
        return result

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
