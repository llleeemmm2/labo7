import json
import csv
import sys
import os


def json_to_csv(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    filename = os.path.splitext(json_file)[0]

    if isinstance(data, list):
        headers = data[0].keys()

        with open(f'{filename}.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    else:
        headers = data.keys()

        with open(f'{filename}.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerow(data)

    print(f'Преобразование JSON в CSV завершено. Результирующий файл: {filename}.csv')


if len(sys.argv) != 2:
    print('Формат вызова программы: python json2csv.py example.json')
else:
    json_file = sys.argv[1]
    json_to_csv(json_file)