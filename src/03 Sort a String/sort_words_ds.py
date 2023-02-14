def sort_words(words_to_sort):
    return ' '.join(sorted(words_to_sort.split(), key=str.casefold))


if __name__ == '__main__':
    print(sort_words("banana ORANGE apple"))
