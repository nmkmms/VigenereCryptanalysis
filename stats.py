from scipy.spatial.distance import cosine as distance
from collections import Counter

letterFreq = {
    'a': 8.12, 'b': 1.49, 'c': 2.71,
    'd': 4.32, 'e': 12.0, 'f': 2.30,
    'g': 2.03, 'h': 5.92, 'i': 7.31,
    'j': 0.10, 'k': 0.69, 'l': 3.98,
    'm': 2.61, 'n': 6.95, 'o': 7.68,
    'p': 1.82, 'q': 0.11, 'r': 6.02,
    's': 6.28, 't': 9.10, 'u': 2.88,
    'v': 1.11, 'w': 2.09, 'x': 0.17,
    'y': 2.11, 'z': 0.07
}
freq_list = [letterFreq[key] for key in sorted(letterFreq.keys())]


def text_statistics(text):
    """Get vector of characters usage in given text."""
    clear_text = text.replace(' ', '').lower()
    text_length = len(clear_text)
    counter = Counter(clear_text)

    text_freq_list = [counter[key] if key in counter.keys() else 0 for key in sorted(letterFreq.keys())]
    text_freq_list = [x / text_length * 100 for x in text_freq_list]

    return text_freq_list


def compare(stat_vector):
    """Compare character usage vectors using cosine distance."""
    return 1 - distance(freq_list, stat_vector)
