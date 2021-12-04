class FileObject:

    def __init__(self):
        self.file = 'file.txt'

    def __del__(self):
        print(f'{self.file} - del')
        del self.file


a = FileObject()
print(a)


