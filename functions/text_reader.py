import re


def find_sentences_in_message(message: str, keyword: str):
    """
    Ищет предложения в сообщении, содержащие заданное слово.

    :param message: Сообщение, в котором будет производиться поиск.
    :param keyword: Слово для поиска в предложениях.
    :return: Список предложений, содержащих заданное слово.
    """
    # Регулярное выражение для поиска предложений
    sentences = re.split(r'(?<=[.!?]) +', message)

    # Фильтруем предложения, содержащие ключевое слово
    matching_sentences = [sentence for sentence in sentences if keyword.lower() in sentence.lower()]

    return matching_sentences

