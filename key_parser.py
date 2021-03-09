"""Parse keys from given dictionary file."""


def parse_keys(filename):
    with open(filename, 'r') as in_file:
        keys_ = in_file.read().split('\n')
        return keys_


if __name__ == '__main__':
    keys = parse_keys('dictionary.txt')
    print(keys[:10])