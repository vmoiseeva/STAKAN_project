from flask import Flask, render_template, url_for
import os
from utils.file_counter import count_files
from utils.get_top_10_extensions import get_extensions, get_top_10_ext
from utils.find_largest_files import get_file_size
import time

app = Flask(__name__)

# path to database we are working with
database_path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/test_data.db'

@app.route('/')
@app.route("/home")
def index():
    modification_time = os.path.getmtime(database_path)
    modification_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time))
    total_files = count_files(database_path)
    return render_template('index.html', indexing_time=modification_time_str, total_files=total_files)

@app.route('/statistics_by_extensions')
def statistics_by_extensions():
    dict_of_ext = get_extensions(database_path)
    top_10_ext = get_top_10_ext(dict_of_ext)

    return render_template('stat_by_extension.html', top_10_ext=top_10_ext)

@app.route('/statistics_by_size')
def top_10_statistics_by_size():
    list_of_largest_files = get_file_size(database_path)

    # Convert sizes to gigabytes
    list_of_largest_files_gb = [(file, round(size / (1024 ** 3), 4)) for file, size in list_of_largest_files]

    return render_template('stat_by_size.html', list_of_largest_files=list_of_largest_files_gb)

if __name__ == '__main__':
    app.run(debug=True)