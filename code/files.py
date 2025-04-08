import os.path
from pathlib import Path


class Files:
    """Class for working with strings - file paths. The constructor takes one argument - path of file.
    If path contains only name of the file, it is considered, that file is existing in current directory"""

    def __init__(self, path: str, exist: bool = True):
        if path.count('/') == 0:
            path = str(Path.cwd()) + '/' + path
        if not os.path.isfile(path) and exist:
            print("No such file in this directory")
            exit(1)
        self.path = path

    def get_path(self) -> str:
        """Returns path to the file"""

        return os.path.dirname(self.path)

    def get_name_with_extension(self) -> str:
        """Returns name of current file with the extension of this file"""

        return os.path.basename(self.path)

    def get_name_without_extension(self) -> str:
        """Returns only name of the file, without extension"""

        return list(os.path.basename(self.path).split('.'))[0]

    def get_extension(self) -> str:
        """Returns the extension of the file"""

        return list(os.path.basename(self.path).split('.'))[1]

    def write(self, data) -> None:
        """Clears file and writes data to the file"""

        file = open(self.path, 'w')
        file.write(data)
        file.close()

    def read(self) -> str:
        """Reads data from the current file and returns string with this data"""

        file = open(self.path, 'r')
        data = file.read()
        file.close()
        return data

