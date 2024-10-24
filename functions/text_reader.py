import re

class TextReader():
    text: str
    word: str
    def __init__(self, text, word):
        self.text = text
        self.word = word
    def text_reader(self):
        sentences = re.split(r'(?<=[.!?]) +', self.text)
        matching_sentences = [i for i in sentences if self.word.lower() in i.lower()]
        return matching_sentences

    def send_matching_sentences(self):
        sentences = self.text_reader()
        message = f'Слово {self.word} было найдено {len(sentences)} раз:\n'
        for i in range(len(sentences)):
            message += f'\n{i+1} Предложение: {sentences[i]}'
        return message




