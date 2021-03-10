import re
from vigenere_cipher import vigenere
from key_parser import parse_keys
from stats import text_statistics, compare, letterFreq
from random import choice, choices
from string import ascii_lowercase as letters


PLAINTEXT = """
Cryptanalysis is the study of analyzing information systems in order to 
study the hidden aspects of the systems. Cryptanalysis is used to breach 
cryptographic security systems and gain access to the contents of encrypted 
messages, even if the cryptographic key is unknown.
In addition to mathematical analysis of cryptographic algorithms, 
cryptanalysis includes the study of side-channel attacks that do not target 
weaknesses in the cryptographic algorithms themselves, but instead exploit 
weaknesses in their implementation.
Even though the goal has been the same, the methods and techniques of 
cryptanalysis have changed drastically through the history of cryptography, 
adapting to increasing cryptographic complexity, ranging from the pen-and-paper 
methods of the past, through machines like the British Bombes and Colossus 
computers at Bletchley Park in World War II, to the mathematically advanced 
computerized schemes of the present. Methods for breaking modern cryptosystems 
often involve solving carefully constructed problems in pure mathematics, the 
best-known being integer factorization. """

# Secret is randomly generated from dictionary.txt file or entered
SECRET = None

# Number of keys to choose from dictionary
NUMBER_OF_KEYS = 1000


def generate_secret(keys):
    """Generate secret from given keys."""
    global SECRET
    SECRET = choice(keys)


def main():
    keys = choices(parse_keys('dictionary.txt'), k=NUMBER_OF_KEYS)
    if not SECRET:
        generate_secret(keys)

    plaintext = re.sub(r'[\.,\-\n!:?]', '', PLAINTEXT)
    cipher = vigenere(plaintext, SECRET)
    print(f'CIPHERTEXT:\n{cipher}')

    keys.sort(key=lambda x: -compare(text_statistics(vigenere(cipher, x, dec=True))))
    best_key = keys[0]
    stats = text_statistics(vigenere(cipher, keys[0], dec=True))
    best_key_stat = compare(stats)
    print(f'Best key: `{best_key}` . Result for best key: {best_key_stat:.6f}\n')
    print(f'Statistic for `{best_key}` key:\n{dict(zip(letters, stats))}\n')
    print(f'Standard letter frequency:\n{letterFreq}')

    assert SECRET == best_key


if __name__ == '__main__':
    main()
