import PyPDF2

class PDFMuse:
    ex = [".pdf"]

    def get_meta_inf(self, path):
        metadata = {}
        try:
            with open(path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_pages = len(pdf_reader.pages)

            metadata["Pages"] = num_pages

        except (FileNotFoundError, PermissionError):
            pass

        return metadata

# if __name__ == "__main__":
#     # Create an instance of the class with the path to the CSV file
#     collector = PDFMuse()
#
#     # Collect and add file meta information to the CSV
#     print(collector.get_meta_inf('/Users/valeriiamoiseeva/Downloads/Статистика ДЗ №3.pdf'))