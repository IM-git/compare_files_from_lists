import json


class ReadFile:

    @staticmethod
    def read_file(path):
        with open(path) as text:
            data = text.read()
        return data

    @staticmethod
    def read_json_file(way):
        with open(way) as text:
            data = json.load(text)
        return data


if __name__ == '__main__':
    PATH = "../filelist.txt"
    PATH_JSON = "../menu.json"

    print(ReadFile.read_file(PATH))
    print(ReadFile.read_json_file(PATH_JSON))
