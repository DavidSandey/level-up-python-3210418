import json


def save_dict(dic_to_save, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        json.dump(dic_to_save, file, indent=4)


def load_dict(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


if __name__ == '__main__':
    dictionary = {'a': True, 'b': [1, 'banana'], 'c': None}
    print(dict(dictionary))
    FILENAME = "dictionary.json"
    save_dict(dictionary, FILENAME)

    dictionary2 = load_dict(FILENAME)
    print(dict(dictionary2))
