import os
import time
import pandas as pd


def count_files(path, csv_file):
    file_counter = 0

    # Check if the CSV file exists
    if os.path.exists(csv_file):
        # Get the file's modification time
        file_modification_time = os.path.getmtime(csv_file)

        # Calculate the current time
        current_time = time.time()

        # Check if the CSV file was modified more than two days ago
        if current_time - file_modification_time > 2 * 24 * 3600:
            print("Warning: The CSV file should be updated.")

        # Read the CSV file using pandas
        df = pd.read_csv(csv_file)

        # Count the number of rows (files) in the CSV
        file_counter = len(df)

    return file_counter


if __name__ == "__main__":
    start_time = time.time()
    path = '/Users/valeriiamoiseeva/PycharmProjects/STAKAN_project'
    csv_file = 'file_data.csv'

    total_files = count_files(path, csv_file)
    end_time = time.time()

    print(f"Total files on your hard drive: {total_files}")
    print(f"Program execution time:{end_time - start_time:.2f} seconds")
