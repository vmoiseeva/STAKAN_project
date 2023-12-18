import os
import sqlite3
from os.path import splitext
from filesmeta.apollo import Apollo
from filesmeta.history_muse import HistoryMuse
from filesmeta.img_muse import IMGMuse
from filesmeta.pdf_muse import PDFMuse
from filesmeta.ms_office_muse import MSOfficeMuse

class Completist:
    def __init__(self, root_folder, database_path):
        self.root_folder = root_folder
        self.file_data = []
        # path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs'
        # filename = 'test_data.csv'
        self.database_path = database_path

        # Initialize Apollo dispatcher
        self.apollo_dispatcher = Apollo()

        # Initialize its Muses
        self.apollo_dispatcher.add_muse(PDFMuse())
        self.apollo_dispatcher.add_muse(IMGMuse())
        self.apollo_dispatcher.add_muse(HistoryMuse())
        self.apollo_dispatcher.add_muse(MSOfficeMuse())

    # здесь вместо того, чтобы обрабатывать массив файлов в цикле, извлекая их них информацию,
    # предлагается написать генератор, который создает такой объект, из которого по одному
    # можно получать файлы и обрабатывать их
    # ПЕРЕПИСАТЬ КОД
    def get_file_info_generator(self):
        for root, _, files_list in os.walk(self.root_folder):
            for filename in files_list:
                file_path = os.path.join(root, filename)
                ext = splitext(file_path)[1] or '.no_extension'

                # Use the Apollo dispatcher to get metadata
                file_file_overview = self.apollo_dispatcher.get_meta_inf(file_path)

                yield file_file_overview

    def process_files(self):
        for file_info in self.get_file_info_generator():
            # Process the files one by one
            self.save_to_database(file_info)

    def save_to_database(self, file_info):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        # Create table if doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT,
                file_size INTEGER,
                file_path TEXT,
                creation_date TEXT,
                modification_date TEXT,
                image_width INTEGER,
                image_height INTEGER,
                pages INTEGER,
                slides INTEGER,
                sheets INTEGER
            )
        ''')

        # Insert metadata into the DB
        cursor.execute('''
            INSERT INTO file_metadata (
                file_name, file_size, file_path, creation_date, modification_date,
                image_width, image_height, pages, slides, sheets
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            file_info.get('File Name', ''),
            file_info.get('File Size', 0),
            file_info.get('File Path', ''),
            file_info.get('Creation Date', ''),
            file_info.get('Modification Date', ''),
            file_info.get('Image Width', 0),
            file_info.get('Image Height', 0),
            file_info.get('Pages', 0),
            file_info.get('Slides', 0),
            file_info.get('Sheets', 0)
        ))

        # Save changes and close connection
        conn.commit()
        conn.close()

if __name__ == '__main__':
    root_folder = '/Users/valeriiamoiseeva/Downloads'
    database_path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/database.db'
    completist = Completist(root_folder, database_path)
    completist.process_files()