import os
from datetime import datetime
import time
import csv


class Completist:
    """ Completist is a person who is extremely interested in a particular subject
    and who wants to collect or experience as many things as possible connected with it,
    so that his or her collection or experience is complete
    """

    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.file_data = []
        path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs'
        filename = 'file_data.csv'
        self.path_to_csv = os.path.join(path, filename)

    def get_file_info(self):
        for root, _, files in os.walk(self.root_folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    file_size = os.path.getsize(file_path)
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                except (FileNotFoundError, PermissionError):
                    pass

                file_info = {
                    'Name': filename,
                    'Full Path': file_path,
                    'Size': file_size,
                    'Creation Date': creation_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'Modification Date': modification_time.strftime('%Y-%m-%d %H:%M:%S')
                }

                self.file_data.append(file_info)

    def write_to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Full Path', 'Size', 'Creation Date', 'Modification Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for file_info in self.file_data:
                writer.writerow(file_info)

    def get_path_to_csv(self):
        return self.path_to_csv


if __name__ == "__main__":
#     start_time = time.time()
#
    completist = Completist('/')
#     completist.get_file_info()
#     output_file = completist.get_path_to_csv()
#     completist.write_to_csv(output_file)
#
#     end_time = time.time()
#     print(f"Program execution time: {end_time - start_time:.2f} seconds")

    # SHORT VERSION OF THE TABLE
    original_csv_path = completist.get_path_to_csv()

    # Specify the path to the new CSV file with the first 50 rows cut
    new_csv_path = '/Users/valeriiamoiseeva/PycharmProjects/STAKAN_project/data/new_filedata.csv'

    # Open the original CSV file for reading and the new CSV file for writing
    with open(original_csv_path, 'r', newline='') as input_csv, open(new_csv_path, 'w', newline='') as output_csv:
        # Create a CSV reader for the input file
        reader = csv.reader(input_csv)

        # Create a CSV writer for the output file
        writer = csv.writer(output_csv)

        # Skip the first 50 rows (header included)
        for i, row in enumerate(reader, start=1):
            if i < 50:
                writer.writerow(row)