import os
from os.path import join, splitext, getsize
from tabulate import tabulate
import time


def get_file_list(root_path):
    """ Формирует список всех файлов, их расширений и путей к ним в заданной директории и во всех ее субдиректориях """

    file_list = []

    for root, _, files in os.walk(root_path):
        for filename in files:
            file_path = join(root, filename)
            name, ext = splitext(filename)
            file_list.append((name, file_path, ext))
    return file_list


def get_file_size(file_list, element_index=1):
    """ Добавляет размеры файлов в список файлов
     Принимает на вход список файлов и индекс элемента, в котором содержится путь к файлу
     По умолчанию равен 1, так как в нашем списке путь находится по этому индексу
     """
    updated_file_list = []

    for item in file_list:
        if element_index < len(item):
            file_path = item[element_index]
            try:
                size = getsize(file_path)
                updated_file_list.append((*item, size))
            except (FileNotFoundError, PermissionError):
                pass
        else:
            print("Index out of range for this tuple.")


    return updated_file_list


def get_10_largest(file_list):
    """ Сортирует список по размеру файлов """

    ten_largest_files = sorted(file_list, key=lambda x: x[-1], reverse=True)[:10]

    return ten_largest_files


def create_table(list_of_files):
    table_with_files = []
    for i, (name, file_path, ext, size) in enumerate(list_of_files, start=1):
        size_in_gb = size / (1024 ** 3)  # 1 GB = 1024^3 bytes
        table_with_files.append([i, name, file_path, ext, f"{size_in_gb:.2f} GB"])

    table = tabulate(table_with_files, headers=["#", "Filename", "Path", "Extension", "Size"], tablefmt="fancy_grid")

    return table


if __name__ == "__main__":
    start_time = time.time()
    root_path = os.path.abspath(os.sep)  # получаем доступ к корневой папке
    all_files_list = get_file_list(root_path)
    with_sizes = get_file_size(all_files_list)
    ten_largest = get_10_largest(with_sizes)
    fancy_ten_largest = create_table(ten_largest)
    print("Top 10 largest files:")
    print(fancy_ten_largest)
    end_time = time.time()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")















# def get_10_largest_files(root_path):
#     start_time = time.time()  # замеряем время
#     file_list = []  # список, в который будем складывать путь к файлу и размер этого файла
#
#     for root, _, files in os.walk(root_path):
#         for filename in files:
#             file_path = join(root, filename)  # формируем пусть к файлу
#             try:
#                 file_size = getsize(file_path)  # получаем размер файла, путь к которому сформировали выше
#                 file_list.append((file_path, file_size))  # добавляем полученные данные в список
#             except (FileNotFoundError, PermissionError):
#                 pass
#                 # при запуске кода возникали ошибки - нек-е файлы не находились. Полностью разобраться, почему так происходит, не получилось.
#                 # в итоге решила, что раз файла нет, то и считать ничего не надо, и можно/нужно просто посчитать размеры тех файлов, которые существуют
#                 # но не уверена в правильности своего решения
#
#     ten_largest_files = sorted(file_list, key=lambda x: x[1], reverse=True)[
#                         :10]  # сортируем список по убыванию и обрезаем до 10
#
#     # Создаем список списков, чтобы дальше создать из него красивую таблицу
#     table_ten_largest_files = []
#     for i, (file_path, file_size) in enumerate(ten_largest_files, start=1):
#         table_ten_largest_files.append([i, file_path, f"{file_size} bytes"])
#
#     # Создаем красивую таблицу
#     table = tabulate(table_ten_largest_files, headers=["#", "Path", "Size"], tablefmt="fancy_grid")
#
#     # Замеряем время
#     end_time = time.time()
#     elapsed_time = end_time - start_time  # получаем время, затраченное на исполнение программы
#     return table, elapsed_time
#
#
# if __name__ == "__main__":
#     root_path = os.path.abspath(os.sep) # получаем доступ к корневой папке
#     top_10_table, elapsed_time = get_10_largest_files(root_path)
#     print("Top 10 largest files:")
#     print(top_10_table)
#     print(f"Program execution time: {elapsed_time:.2f} seconds")
