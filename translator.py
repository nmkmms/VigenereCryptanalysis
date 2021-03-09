"""Translate word to array of integers and backwards."""


def to_nums(text: str):
    return [ord(char) - ord('a') if char != ' ' else ' ' for char in text]


def to_char(text_enc: list):
    return ''.join([chr(num + ord('a')) if num != ' ' else ' ' for num in text_enc])


if __name__ == '__main__':
    test_word = 'hello cat'
    assert test_word == to_char(to_nums(test_word))

