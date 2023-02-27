import csv


def merge_csv(list_of_input_paths, output_path):
    field_names = []

    for input_path in list_of_input_paths:
        with open(input_path, 'r', encoding='utf-8') as input_csv_file:
            fields = csv.DictReader(input_csv_file).fieldnames
            field_names.extend(
                field for field in fields if field not in field_names)

    with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=field_names)
        writer.writeheader()
        for input_file in list_of_input_paths:
            with open(input_file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


if __name__ == '__main__':
    merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
