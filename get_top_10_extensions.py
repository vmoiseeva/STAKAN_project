import os
from collections import defaultdict
from os.path import join, splitext
from tabulate import tabulate
import time
import pandas as pd


def get_extensions(path, csv_file):
    ext_dictionary = defaultdict(int)  # заводим словарь, чтобы с его помощью считать расширения
    ext_dictionary['NoExtension'] = 0  # отдельно оговариваем случай, когда у файла не находится расширение

    # Check if the CSV file exists
    if os.path.exists(csv_file):
        # Get the file's modification time
        file_modification_time = os.path.getmtime(csv_file)

        # Calculate the current time
        current_time = time.time()

        # Check if the CSV file was modified more than two days ago
        if current_time - file_modification_time > 2 * 24 * 3600:
            print("Warning: The CSV file should be updated.")

        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)

        for file_path in df['Full Path']:
            ext = splitext(file_path)[1]  # Get the file extension
            if ext == '':
                ext_dictionary['NoExtension'] += 1
            else:
                ext_dictionary[ext] += 1

    return ext_dictionary

def get_top_10_ext(ext_dictionary):
    top_10_extensions_list = sorted(ext_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_extensions_list

def get_fancy_table(top_10_extensions_list):
    # Создаем список списков, чтобы дальше создать из него красивую таблицу
    table_top_10_extensions = []
    for i, (extension, count) in enumerate(top_10_extensions_list, start=1):
        table_top_10_extensions.append([i, extension, count])

    # Создаем таблицу
    table = tabulate(table_top_10_extensions, headers=["#", "Extension", "Count"], tablefmt="fancy_grid")

    return table


if __name__ == "__main__":
    start_time = time.time()
    path = '/Users/valeriiamoiseeva/PycharmProjects/STAKAN_project'
    csv_file = 'file_data.csv'

    dict_of_ext = get_extensions(path, csv_file)
    top_10 = get_fancy_table(get_top_10_ext(dict_of_ext))

    end_time = time.time()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print(top_10)
