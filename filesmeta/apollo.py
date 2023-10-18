from os.path import splitext


class Apollo:
    def __init__(self):
        self._extensions = {}

    def add_muse(self, muse):
        ex = muse.ex
        for e in ex:
            self._extensions[e] = muse

    def get_meta_inf(self, file_path):

        ex = splitext(file_path)[1]
        res = self._extensions["*"].get_meta_inf(file_path)

        if ex in self._extensions:
            res.update(self._extensions[ex].get_meta_inf(file_path))
        else:
            res.update({"Comment": "The extension is not supported"})

        return res

    def handle_files(self, file_paths):
        all_metadata = []

        for file_path in file_paths:
            ext = splitext(file_path)[1]

            if ext in self._extensions or '*' in self._extensions:
                metadata = self.get_meta_inf(file_path)
            else:
                metadata = {"Comment": "The extension is not supported"}
            all_metadata.append(metadata)

        return all_metadata
