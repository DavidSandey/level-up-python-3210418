def index_all(list_to_index, value_to_find):
    indexes = []
    for index, item in enumerate(list_to_index):
        if item == value_to_find:
            indexes.append([index])
        elif isinstance(list_to_index[index], list):
            for i in index_all(list_to_index[index], value_to_find):
                indexes.append([index] + i)
    return indexes


if __name__ == "__main__":
    print(index_all([1, [2, 1], [0, [0, 2, 1]], 1], 1))
