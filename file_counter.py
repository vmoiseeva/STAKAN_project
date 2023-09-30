import os
from os.path import join, isfile
import time


def count_files(path):
    file_counter = 0  # заводим счетчик для подсчета файлов

    for root, _, files in os.walk(path):
        for filename in files:
            file_path = join(root, filename)
            if isfile(file_path):  # проверяем, является ли файлом рассматриваемый элемент
                file_counter += 1  # считаем его, если да

    return file_counter


if __name__ == "__main__":
    start_time = time.time()
    path = os.path.abspath(os.sep)  # получаем доступ к корневой папке
    total_files = count_files(path)
    end_time = time.time()

    print(f"Total files on your hard drive: {total_files}")
    print(f"Program execution time:{end_time - start_time:.2f} seconds")
