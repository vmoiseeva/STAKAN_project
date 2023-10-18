import os
from os.path import splitext
import csv
from filesmeta.apollo import Apollo

class Completist:
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.file_data = []
        path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs'
        filename = 'test_data.csv'
        self.path_to_csv = os.path.join(path, filename)

        # Initialize Apollo dispatcher
        self.apollo_dispatcher = Apollo()

    def get_file_info(self):
        for root, _, files in os.walk(self.root_folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                ext = splitext(file_path)[1] or '.no_extension'
                print(ext)

                if ext not in self.apollo_dispatcher._extensions:
                    print(f"Skipping unsupported file: {file_path}")
                    continue

                # Use the Apollo dispatcher to get metadata
                file_file_overview = self.apollo_dispatcher.get_meta_inf(file_path)
                print(f"Processed file: {file_path}")
                print(f"Metadata: {file_file_overview}")

                self.file_data.append(file_file_overview)

    def write_to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            # Get the fieldnames from the metadata dictionaries
            fieldnames = set()
            for file_info in self.file_data:
                fieldnames.update(file_info.keys())

            writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))

            writer.writeheader()
            for file_info in self.file_data:
                writer.writerow(file_info)

    def get_path_to_csv(self):
        return self.path_to_csv

if __name__ == '__main__':
    root_folder = '/Users/valeriiamoiseeva/Downloads'  # Replace with the actual root folder path
    completist = Completist(root_folder)
    completist.get_file_info()  # Gather metadata for files in the root folder
    output_csv_path = completist.get_path_to_csv()
    completist.write_to_csv(output_csv_path)  # Write the metadata to a CSV file