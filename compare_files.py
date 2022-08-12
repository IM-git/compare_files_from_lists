from tools.read_file import ReadFile
from tools.create_file import CreateFile
from tools.file_correction import FileCorrection
from tools.base_exeption import BaseExceptions

PATH = 'menu.json'
DATA = ReadFile.read_json_file(PATH)


class CompareFiles:
    """
    There are using the initialization JSON file.
    Performing file comparison.
    Creating new file with missing paths.
    """

    def __init__(self):

        self.compared_file = FileCorrection.deleting_beginning_of_part(
            text=ReadFile.read_file(DATA["compared_list"]),
            del_part=DATA["compared_part_to_be_deleted"])

        self.main_file = FileCorrection.deleting_beginning_of_part(
            text=ReadFile.read_file(DATA["main_list"]),
            del_part=DATA["main_part_to_be_deleted"])

        self.new_file_path = DATA["new_file_with_parts"]

    def compare_files(self):
        """Creates a list with missing paths from compared lists."""
        text = ''

        for path in self.main_file.split('\n'):
            if path not in self.compared_file.split('\n'):
                #   +Returning the deleted part back
                text += DATA["main_part_to_be_deleted"] + path + '\n'
            else:
                pass
        return text

    def create_file(self):
        try:
            CreateFile().create_file(self.new_file_path, self.compare_files())
        except BaseExceptions:
            print("Something wrong! Check the files.")


if __name__ == '__main__':
    PATH1 = "./filelist1.txt"
    PATH2 = "./filelist2.txt"
    NEW_FILE_PATH = "./text_text.txt"
    DELETE_PART1 = 'X:\\test folder\\'
    DELETE_PART2 = 'X:\\test folder\\'
    FILE1 = 'X:\\test folder\\1 ' \
            'X:\\test folder\\2 ' \
            'X:\\test folder\\case.txt '
    FILE2 = 'X:\\test folder\\1 ' \
            'X:\\test folder\\case.txt '

    CompareFiles().create_file()
