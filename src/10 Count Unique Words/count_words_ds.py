import re
from collections import Counter


def count_words(path):
    with open(path, "r", encoding="utf-8") as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.lower() for word in all_words]
        print(f"Total word count = {len(all_words)}")

        word_counts = Counter(all_words)

        print(f"Top 20 words in {path}")
        for word in word_counts.most_common(20):
            print(f"{word[0]}\t{word[1]}")


if __name__ == "__main__":
    count_words("pg10.txt")
