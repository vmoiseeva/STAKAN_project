import os
from os.path import join, isfile
import time


def count_files(path):
    start_time = time.time()
    file_counter = 0  # заводим счетчик для подсчета файлов

    for root, _, files in os.walk(path):
        for filename in files:
            file_path = join(root, filename)
            if isfile(file_path):  # проверяем, является ли файлом рассматриваемый элемент
                file_counter += 1  # считаем его, если да

    end_time = time.time()
    elapsed_time = end_time - start_time

    return file_counter, elapsed_time


if __name__ == "__main__":
    path = os.path.abspath(os.sep)  # получаем доступ к корневой папке
    total_files, elapsed_time = count_files(path)
    print(f"Total files on your hard drive: {total_files}")
