import os
from os.path import join, splitext
from tabulate import tabulate
import time


def get_top_10_extensions(path):
    start_time = time.time()
    ext_dictionary = dict()  # заводим словарь, чтобы с его помощью считать расширения
    ext_dictionary['NoExtension'] = 0  # отдельно оговариваем случай, когда у файла не находится расширение

    for root, _, files in os.walk(path):
        for filename in files:
            file_path = join(root, filename)
            ext = splitext(file_path)[1]  # получаем расширение
            if ext == '':
                ext_dictionary['NoExtension'] += 1  # введем отдельный счетчик для файлов, у которых нет расширения
                # насколько я понимаю, это в основном системные файлы, и поэтому я решила их не считать,
                # решив, что сейчас нас интересуют файлы, которыми мы пользуемся (документы, фото и т.п.)
                # но я полагаю, что если цель - изучить вообще все возможные файлы, придется разбираться
                # и в типах системных файлов (но это уже, насколько я понимаю, не то же самое, что считать расширения)
            else:
                if ext in ext_dictionary:
                    ext_dictionary[ext] += 1
                else:
                    ext_dictionary[ext] = 1

    top_10_extensions_list = sorted(ext_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]

    # Создаем список списков, чтобы дальше создать из него красивую таблицу
    table_top_10_extensions = []
    for i, (extension, count) in enumerate(top_10_extensions_list, start=1):
        table_top_10_extensions.append([i, extension, count])

    # Создаем таблицу
    table = tabulate(table_top_10_extensions, headers=["#", "Extension", "Count"], tablefmt="fancy_grid")

    # Считаем время, затраченное на выполнение программы
    end_time = time.time()
    elapsed_time = end_time - start_time

    return table, elapsed_time


if __name__ == "__main__":
    root_path = os.path.abspath(os.sep) # получаем доступ к корневой папке
    top_10_extensions, elapsed_time = get_top_10_extensions(root_path)
    print("Top 10 extensions:")
    print(top_10_extensions)
    print(f"Program execution time: {elapsed_time:.2f} seconds")
