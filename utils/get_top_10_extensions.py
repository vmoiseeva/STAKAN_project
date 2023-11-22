import os
from collections import defaultdict
from tabulate import tabulate
import time
import sqlite3


def get_extensions(database_path):
    ext_dictionary = defaultdict(int)  # Create a dictionary to count extensions

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Run a query to retrieve extension data
    cursor.execute("SELECT file_path FROM file_metadata")
    result = cursor.fetchall()

    conn.close()

    for row in result:
        file_path = row[0]
        file_extension = os.path.splitext(file_path)[1] if os.path.splitext(file_path)[1] else 'NoExtension'
        ext_dictionary[file_extension] += 1

    return ext_dictionary

def get_top_10_ext(ext_dictionary):
    top_10_extensions_list = sorted(ext_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_extensions_list

def get_fancy_table(top_10_extensions_list):
    # Create a list of lists to further create a table
    table_top_10_extensions = []
    for i, (extension, count) in enumerate(top_10_extensions_list, start=1):
        table_top_10_extensions.append([i, extension, count])

    # Create a table
    table = tabulate(table_top_10_extensions, headers=["#", "Extension", "Count"], tablefmt="fancy_grid")

    return table


if __name__ == "__main__":
    start_time = time.time()

    from staff.completist import Completist

    root_folder = '/Users/valeriiamoiseeva/Downloads'
    database_path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/database.db'

    completist = Completist(root_folder, database_path)

    dict_of_ext = get_extensions(database_path)
    top_10 = get_fancy_table(get_top_10_ext(dict_of_ext))

    end_time = time.time()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
    print(top_10)
