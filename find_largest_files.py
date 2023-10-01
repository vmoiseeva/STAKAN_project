import os
from os.path import getsize
from tabulate import tabulate
import pandas as pd
import time

"""
Проблема с кодом: выдает файлы-дубликаты (?). Файл один, путей к нему -- два
"""


def get_file_size(full_path):
    file_list = []  # список, в который будем складывать путь к файлу и размер этого файла

    # Check if the CSV file exists
    if os.path.exists(full_path):
        # Get the file's modification time
        file_modification_time = os.path.getmtime(full_path)

        # Calculate the current time
        current_time = time.time()

        # Check if the CSV file was modified more than two days ago
        if current_time - file_modification_time > 2 * 24 * 3600:
            print("Warning: The CSV file should be updated.")

        # Read the CSV file using pandas
        df = pd.read_csv(full_path)

        for file_path in df['Full Path']:
            try:
                file_size = getsize(file_path)  # получаем размер файла, путь к которому сформировали выше
                file_list.append((file_path, file_size))  # добавляем полученные данные в список
            except (FileNotFoundError, PermissionError):
                pass
    return file_list


def get_10_largest(file_list):
    ten_largest_files = sorted(file_list, key=lambda x: x[1], reverse=True)[
                        :10]  # сортируем список по убыванию и обрезаем до 10
    return ten_largest_files


def get_fancy_filetable(ten_largest_files):
    # Создаем список списков, чтобы дальше создать из него красивую таблицу
    table_ten_largest_files = []
    for i, (file_path, file_size) in enumerate(ten_largest_files, start=1):
        table_ten_largest_files.append([i, file_path, f"{file_size} bytes"]) # выводить в гигабайтах!!!

    # Создаем красивую таблицу
    table = tabulate(table_ten_largest_files, headers=["#", "Path", "Size"], tablefmt="fancy_grid")

    return table


if __name__ == "__main__":
    start_time = time.time()

    from completist import Completist

    completist = Completist('/')

    full_path = completist.get_path_to_csv()

    list_of_files = get_file_size(full_path)
    top_10 = get_fancy_filetable(get_10_largest(list_of_files))

    end_time = time.time()

    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print(top_10)
