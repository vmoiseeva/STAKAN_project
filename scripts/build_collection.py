import os
import time
from staff.completist import Completist
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        return result, current_time, execution_time

    return wrapper

@log_execution_time
def update_database(root_folder, database_path):

    completist = Completist(root_folder, database_path)
    completist.process_files()

if __name__ == "__main__":
    start_time = time.time()

    root_folder = '/Users/valeriiamoiseeva/Downloads'
    database_path = os.path.join(
        '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs',
        'test_data.db'
    )

    result_value, current_time_value, execution_time_value = update_database(root_folder, database_path)
    print(f"Execution time: {execution_time_value:.2f} seconds")
    print(f"Execution datetime: {current_time_value}")