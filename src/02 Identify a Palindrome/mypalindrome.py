from collections import deque
import string


def normalize_word(word):
    # remove punctuation, digits and whitespace and convert to lower case
    word = word.translate(str.maketrans(
        '', '', string.punctuation + string.digits + string.whitespace)).lower()

    return word


def is_palindrome(word):

    d = deque(normalize_word(word))

    while len(d) > 1:
        first_letter = d.popleft()
        last_letter = d.pop()
        if first_letter != last_letter:
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
