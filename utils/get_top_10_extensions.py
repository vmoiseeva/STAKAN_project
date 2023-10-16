import os
from collections import defaultdict
from os.path import splitext
from tabulate import tabulate
import time
import pandas as pd


def get_extensions(full_path):
    ext_dictionary = defaultdict(int)  # Create a dictionary to count extensions

    # Check if the CSV file exists
    if os.path.exists(full_path):
        # Get the file's modification time
        file_modification_time = os.path.getmtime(full_path)

        # Calculate the current time
        current_time = time.time()

        # Check if the CSV file was modified more than two days ago
        if current_time - file_modification_time > 2 * 24 * 3600:
            print("Warning: The CSV file should be updated.")

            df = pd.read_csv(full_path)

            # Extract the extension from the file path
            df['File Extension'] = df['Full Path'].apply(lambda x: splitext(x)[1] if splitext(x)[1] else 'NoExtension')

            # Count ext and update the dictionary
            ext_counts = df['File Extension'].value_counts().to_dict()
            ext_dictionary.update(ext_counts)

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

    from staff.completist import Completist

    completist = Completist('/')

    full_path = completist.get_path_to_csv()

    dict_of_ext = get_extensions(full_path)
    top_10 = get_fancy_table(get_top_10_ext(dict_of_ext))

    end_time = time.time()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print(top_10)
