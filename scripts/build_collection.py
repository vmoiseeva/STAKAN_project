import os
import time
from staff.completist import Completist

def update_database(root_folder, database_path):
    completist = Completist(root_folder)

    completist.get_file_info()
    completist.create_csv(database_path)

if __name__ == "__main__":
    start_time = time.time()

    root_folder = '/Users/valeriiamoiseeva/Downloads'
    database_path = os.path.join(
        '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs',
        'test_data.csv'
    )

    # Call the update_database function
    update_database(root_folder, database_path)

    end_time = time.time()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")