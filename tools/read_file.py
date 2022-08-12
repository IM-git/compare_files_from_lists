PATH = "../filelist.txt"


class ReadFile:

    @staticmethod
    def read_file(path):
        with open(path) as text:
            data = text.readlines()
        return data


if __name__ == '__main__':
    print(ReadFile.read_file(PATH))
