"""Vigenere cipher realization."""
from translator import *


def vigenere(text, secret, dec=False):
    word_encoded = to_nums(text.lower())
    long_secret = secret * (len(word_encoded) // len(secret) + 1)
    long_secret_enc = to_nums(long_secret.lower())[::-1]

    cipher = []
    for char in word_encoded:
        if char == ' ':
            cipher.append(' ')
        else:
            cipher.append((char + long_secret_enc.pop()) % 26 if not dec
                          else (char - long_secret_enc.pop()) % 26)

    return to_char(cipher)


if __name__ == '__main__':
    plain = 'Hello world'
    sec = 'kek'
    assert plain.lower() == vigenere(vigenere(plain, sec), sec, enc=False)
