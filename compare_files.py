from tools.read_file import ReadFile
from tools.create_file import CreateFile
from tools.base_exeption import BaseExceptions


PATH1 = "./filelist1.txt"
PATH2 = "./filelist2.txt"
PATH = "./text_text.txt"


class CompareFiles:

    def __init__(self):
        """Mb the better way just delete init and
        add files exactly to method."""
        self.file1 = ReadFile.read_file(PATH1)
        self.file2 = ReadFile.read_file(PATH2)
        self.text = ''

    def compare_files(self):
        text = ''
        try:
            for x in self.file2:
                if x not in self.file1:
                    text += x
                    print(x.rstrip())
                else:
                    pass
            return text
        except BaseExceptions:
            print("Something wrong! Check the files.")

    def create_file(self):
        CreateFile().create_file(PATH, self.compare_files())


if __name__ == '__main__':
    CompareFiles().create_file()
