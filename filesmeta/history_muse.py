import os
from datetime import datetime

class HistoryMuse:
    ex = ["*"]

    def get_meta_inf(self, path):
        metadata = {}

        if os.path.exists(path):
            try:
                file_size = os.path.getsize(path)
                creation_date = datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y-%m-%d %H:%M:%S")
                modification_date = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M:%S")

                metadata["File Name"] = os.path.basename(path)
                metadata["File Size"] = file_size
                metadata["File Path"] = path
                metadata["Creation Date"] = creation_date
                metadata["Modification Date"] = modification_date
            except (FileNotFoundError, PermissionError):
                pass

        return metadata
