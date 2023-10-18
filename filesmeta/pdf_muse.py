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
