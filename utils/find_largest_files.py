# import os
import sqlite3
from tabulate import tabulate
import time

"""
Надо проверить: иногда выдает файлы-дубликаты (?). Файл один, путей к нему -- два
"""


def get_file_size(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # # Check if the CSV file exists
    # if os.path.exists(full_path):
    #     # Get the file's modification time
    #     file_modification_time = os.path.getmtime(full_path)
    #
    #     # Calculate the current time
    #     current_time = time.time()
    #
    #     # Check if the CSV file was modified more than two days ago
    #     if current_time - file_modification_time > 2 * 24 * 3600:
    #         print("Warning: The CSV file should be updated.")

    # Get the path and size of the largest file in the database
    cursor.execute("SELECT file_path, file_size FROM file_metadata ORDER BY file_size DESC LIMIT 10")
    results = cursor.fetchall()

    conn.close()

    return results

def get_fancy_filetable(ten_largest_files):
    # Create a list of lists to further create a beautiful table from it
    table_ten_largest_files = []
    for i, (file_path, file_size) in enumerate(ten_largest_files, start=1):
        table_ten_largest_files.append([i, file_path, "{:.4f} GB".format(file_size / (1024 ** 3))])

    # Create fancy table
    table = tabulate(table_ten_largest_files, headers=["#", "Path", "Size"], tablefmt="fancy_grid")

    return table


if __name__ == "__main__":
    start_time = time.time()

    from staff.completist import Completist

    root_folder = '/Users/valeriiamoiseeva/Downloads'
    database_path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/database.db'

    completist = Completist(root_folder, database_path)
    list_of_largest_files = get_file_size(database_path)
    fancy_top_10 = get_fancy_filetable(list_of_largest_files)

    end_time = time.time()

    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print(fancy_top_10)
