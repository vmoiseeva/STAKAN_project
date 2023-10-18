from filesmeta.history_muse import HistoryMuse
from filesmeta.img_muse import IMGMuse
from filesmeta.pdf_muse import PDFMuse
from os.path import splitext


class Apollo:
    def __init__(self):
        self._extensions = {}

    def add_muse(self, muse):
        ex = muse.ex
        for e in ex:
            self._extensions[e] = muse

    def get_meta_inf(self, file_path):
        res = {}
        ex = splitext(file_path)[1]

        if ex in self._extensions:
            res = self._extensions[ex].get_meta_inf(file_path)
        else:
            res = {"error": "The extension is not supported"}

        return res

    def handle_files(self, file_paths):
        all_metadata = []

        for file_path in file_paths:
            ext = splitext(file_path)[1]
            print(f"Processing file: {file_path}")
            print(f"File extension: {ext}")
            if ext in self._extensions:
                metadata = self.get_meta_inf(file_path)
                print(f"Metadata: {metadata}")
            else:
                metadata = {"error": "The extension is not supported"}
            all_metadata.append(metadata)

        return all_metadata


a = Apollo()

m1 = HistoryMuse()  # Create an instance of HistoryMuse
m2 = IMGMuse()      # Create an instance of IMGMuse
m3 = PDFMuse()      # Create an instance of PDFMuse

a.add_muse(m1)
a.add_muse(m2)
a.add_muse(m3)

file_paths = [
    '/Users/valeriiamoiseeva/Documents/Studies/PANDAN/year_2/Prog_techs/test_data.csv',
    '/Users/valeriiamoiseeva/Downloads/IMG_5417.heic'
]

print(a.handle_files(file_paths))
