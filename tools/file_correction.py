class FileCorrection:
    """In this class take string convert in list
    without the specified part and
    convert again in string"""

    @staticmethod
    def deleting_beginning_of_part(text: str, del_part: str):
        new_text = text.split(del_part)
        return ''.join(new_text).strip().lstrip()


if __name__ == '__main__':
    TEXT = 'X:\\test folder\\copy\\2\\PC\\5.txt ' \
           'X:\\test folder\\copy\\2\\PC\\folder 1 ' \
           'X:\\test folder\\copy\\2\\PC\\folder 2'
    DEL = 'X:\\test folder\\'

    print(FileCorrection.deleting_beginning_of_part(TEXT, DEL))
