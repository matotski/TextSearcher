import re

from aiofiles.os import replace


class TextReader():
    text: str
    word: str
    def __init__(self, text, word):
        self.text = text
        self.word = word
    def text_reader(self):
        sentences = self.text.replace("\n","")
        sentences = re.split(r'(?<=[.!?]) +', sentences)
        matching_sentences = [i for i in sentences if self.word.lower() in i.lower()]
        return matching_sentences

    def send_matching_sentences(self):
        sentences = self.text_reader()
        if len(sentences) == 0:
            return "Данное слово не было найдено в тексте ;(w"
        message = f'Слово {self.word} было найдено {len(sentences)} раз:\n'
        for i in range(len(sentences)):
            message += f'\n\n{i+1} Предложение: {sentences[i]}'
        return message




