import os
import tkinter as tk
from tkinter import messagebox, Text
from utils.file_counter import count_files
import time
import sqlite3
from utils.find_largest_files import get_file_size
from utils.get_top_10_extensions import get_extensions, get_top_10_ext

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("STAKAN")
        self.database_path = '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/test_data.db'

        # Create the main menu
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Statistics menu
        statistics_menu = tk.Menu(menu_bar, tearoff=0)
        statistics_menu.add_command(label="Statistics by extensions", command=self.show_statistics_by_extensions)
        statistics_menu.add_command(label="Statistics by size", command=self.show_top_10_statistics_by_size)

        # Add menus to the menu bar
        menu_bar.add_cascade(label="Main Menu", menu=statistics_menu)

        # Display startup information
        total_files, last_indexing_date = self.get_startup_info()
        startup_info_label = tk.Label(root, text=f"Total files indexed: {total_files}\nLast update: {last_indexing_date}")
        startup_info_label.pack(pady=10)

    def get_startup_info(self):
        try:
            total_files = count_files(self.database_path)
        except sqlite3.Error as e:
            print("SQLite error:", e)
            total_files = 0
            last_updated = "N/A"

        last_updated = os.path.getmtime(self.database_path)
        last_updated_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_updated))

        return total_files, last_updated_str

    def show_statistics_by_extensions(self):
        dict_of_ext = get_extensions(self.database_path)
        top_10_ext = get_top_10_ext(dict_of_ext)

        # Convert tuples to strings
        top_10_ext_strings = [f"{extension} - {count}" for extension, count in top_10_ext]

        # Display the results in a Text widget
        result_text = "\n".join(top_10_ext_strings)
        result_window = tk.Toplevel(self.root)
        result_window.title("Top 10 Extensions")

        text_widget = Text(result_window, wrap=tk.WORD)
        text_widget.insert(tk.END, result_text)
        text_widget.pack(expand=True, fill=tk.BOTH)

    def show_top_10_statistics_by_size(self):
        list_of_largest_files = get_file_size(self.database_path)

        # Convert tuples to strings
        list_of_largest_files = [f"{file_path} - {file_size / (1024 ** 3):.4f} GB" for file_path, file_size in
                                 list_of_largest_files]

        # Display the results in a Text widget
        result_text = "\n".join(list_of_largest_files)
        result_window = tk.Toplevel(self.root)
        result_window.title("Top 10 files by Size")

        text_widget = Text(result_window, wrap=tk.WORD)
        text_widget.insert(tk.END, result_text)
        text_widget.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


