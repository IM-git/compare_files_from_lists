class CreateFile:

    @staticmethod
    def create_file(path: str, text: str):
        with open(path, 'w') as newfile:
            data = newfile.write(text)

        return data


if __name__ == '__main__':
    TEXT = "text1\ntext2\ntext3\ntext4\n"
    PATH = "../text_text.txt"
    print(CreateFile.create_file(PATH, TEXT))
