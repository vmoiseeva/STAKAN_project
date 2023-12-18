from flask import Flask, render_template, url_for
from utils.file_counter import count_files
import time
import os

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
    return 'here is my stat by extension'

@app.route('/top_10_statistics_by_size')
def top_10_statistics_by_size():
    return 'here is my stat by size'

if __name__ == '__main__':
    app.run(debug=True)