import time
from staff.completist import Completist

root_folder = '/'
completist = Completist(root_folder)

def update_database(root_folder, database_path):

    completist.get_file_info()
    completist.write_to_csv(database_path)

if __name__ == "__main__":
    start_time = time.time()

    database_path = completist.get_path_to_csv()

    # Call the update_database function
    update_database(root_folder, database_path)

    end_time = time.time()
    print(f"Program execution time: {end_time - start_time:.2f} seconds")