import secrets


def generate_passwords(num_of_words, wordlist_path="diceware.wordlist.asc"):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

        words = [secrets.choice(word_list) for i in range(num_of_words)]
        return ' '.join(words)


print(generate_passwords(4))
print(generate_passwords(7))
