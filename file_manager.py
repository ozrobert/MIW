# ĆWICZENIE 8

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            file = open(self.file_name, 'r', encoding='utf-8')
            read = file.read()
            return print(read)
        except IOError:
            print("Wystąpił błąd, nie można odczytać pliku.")

    def update_file(self, text_data):
        try:
            file = open(self.file_name, 'a', encoding='utf-8')
            file.write(text_data)
            file.close()
        except IOError:
            print("Wystąpił błąd, nie można zapisać pliku.")
