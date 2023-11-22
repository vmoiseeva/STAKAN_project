# import os
import time
import sqlite3

def count_files(database_path):
    file_counter = 0

    # Connect to the database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM file_metadata")
    result = cursor.fetchone()

    if result:
        file_counter = result[0]

    conn.close()

    return file_counter

# НАДО написать отдельную функцию для проверки существования и актуальности БД, которую
# можно использовать во всех утилитах?
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


if __name__ == "__main__":
    start_time = time.time()

    from staff.completist import Completist

    root_folder = '/Users/valeriiamoiseeva/Downloads'
    database_path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/database.db'

    completist = Completist(root_folder, database_path)
    total_files = count_files(database_path)

    end_time = time.time()

    print(f"Total files on your hard drive: {total_files}")
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
