import os
from os.path import join, getsize
from tabulate import tabulate
import time


def get_10_largest_files(root_path):
    start_time = time.time()  # замеряем время
    file_list = []  # список, в который будем складывать путь к файлу и размер этого файла

    for root, _, files in os.walk(root_path):
        for filename in files:
            file_path = join(root, filename)  # формируем пусть к файлу
            try:
                file_size = getsize(file_path)  # получаем размер файла, путь к которому сформировали выше
                file_list.append((file_path, file_size))  # добавляем полученные данные в список
            except (FileNotFoundError, PermissionError):
                pass
                # при запуске кода возникали ошибки - нек-е файлы не находились. Полностью разобраться, почему так происходит, не получилось.
                # в итоге решила, что раз файла нет, то и считать ничего не надо, и можно/нужно просто посчитать размеры тех файлов, которые существуют
                # но не уверена в правильности своего решения

    ten_largest_files = sorted(file_list, key=lambda x: x[1], reverse=True)[
                        :10]  # сортируем список по убыванию и обрезаем до 10

    # Создаем список списков, чтобы дальше создать из него красивую таблицу
    table_ten_largest_files = []
    for i, (file_path, file_size) in enumerate(ten_largest_files, start=1):
        table_ten_largest_files.append([i, file_path, f"{file_size} bytes"])

    # Создаем красивую таблицу
    table = tabulate(table_ten_largest_files, headers=["#", "Path", "Size"], tablefmt="fancy_grid")

    # Замеряем время
    end_time = time.time()
    elapsed_time = end_time - start_time  # получаем время, затраченное на исполнение программы
    return table, elapsed_time


if __name__ == "__main__":
    root_path = os.path.abspath(os.sep) # получаем доступ к корневой папке
    top_10_table, elapsed_time = get_10_largest_files(root_path)
    print("Top 10 largest files:")
    print(top_10_table)
    print(f"Program execution time: {elapsed_time:.2f} seconds")
