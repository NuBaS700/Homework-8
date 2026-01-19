string_01 = (
    "History is always written by the winners. hen two cultures clash, "
    "the loser is obliterated, and the winner writes the history books-books "
    "which glorify their own cause and disparage the conquered foe. "
    "As Napoleon once said, 'What is history, but a fable agreed upon?"
)

# 1. Количество символов без пробелов
chars_count = len(string_01.replace(' ', ''))
print('Количество символов без пробелов:', chars_count)

# 2. Количество слов
words = string_01.split()
print('Количество слов:', len(words))


# 3. Функция поиска слов по первой букве
def my_func(letter, words):
    letter = letter.lower()
    result = []

    for word in words:
        if word.lower().startswith(letter):
            result.append(word)

    return result


# Пример
print('Слова на букву w:', my_func('w', words))
