import re

def text_reader(text: str, word: str):
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentences_with_message = [i for i in sentences if word.lower() in i.lower()]
    return sentences_with_message





