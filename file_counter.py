import os
import time
import pandas as pd


def count_files(full_path):
    file_counter = 0

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

        # Count the number of rows (files) in the CSV
        file_counter = len(df)

    return file_counter


if __name__ == "__main__":
    start_time = time.time()

    from completist import Completist

    completist = Completist('/')

    full_path = completist.get_path_to_csv()
    total_files = count_files(full_path)
    end_time = time.time()

    print(f"Total files on your hard drive: {total_files}")
    print(f"Program execution time: {end_time - start_time:.2f} seconds")
