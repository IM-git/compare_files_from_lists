import os
import shutil

from tools.base_exeption import BaseExceptions


class DeleteFiles:
    """
    Get a compare_files method text from compare_file.py
    Delete the absence folders/files taken from the list.
    """

    def __init__(self, list_paths: str):
        self.list_paths = list_paths

    def iterating_through_values(self) -> None:
        """Use loop for validate that is file/dir and
        delete them."""
        for value in self.list_paths.split('\n'):
            try:
                if os.path.isfile(value):
                    self.delete_file(value)
                elif os.path.isdir(value):
                    self.delete_folder(value)
                else:
                    print(f"File: {value}, empty or isn't defined")
            except BaseExceptions:
                print('Something wrong! Check the files.')

    @staticmethod
    def delete_file(path_to_file: str) -> None:
        os.remove(path_to_file)

    @staticmethod
    def delete_folder(path_to_file: str) -> None:
        shutil.rmtree(path_to_file)


if __name__ == '__main__':
    from tools.read_file import ReadFile

    PATH = 'menu.json'
    DATA = ReadFile.read_json_file(PATH)
    LIST_MISSING_FILES = ReadFile.read_file(DATA["new_file_with_parts"])

    DeleteFiles(LIST_MISSING_FILES).iterating_through_values()
