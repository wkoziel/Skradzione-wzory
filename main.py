import os

class File:
    def __init__(self, data):
        """Klasa przechowuje obiekty plików tex"""
        self._separate(data)
        self.math = [] #Lista zawierająca odseparowane wzory

    def _separate(self, data):
        """Funkcja oddziela tekst od wzorów i zapisuje tylko wzory"""
        pass


class File_Reader:
    def __init__(self):
        """Klasa zawierająca funkcje odpowiedzialne za odczyt plików z bazy i tworzenie dla nich
        obiektów File -- Wersja lokalna algorytmu, będzie on do przerobienia"""
        self.files = [] 
        self.files_names = []
        self._names_download()
        self._read_file()

    def _names_download(self):
        """Pobiera nazwy plików z /database"""
        self.files_names = os.listdir('database')


    def _read_file(self):
        """Wczytuje zawartość plików i tworzy dla nich obiekty File"""
        for file in self.files_names:
            f = open("database/" + file,"r")
            self.files.append(File(f.read()))


def main():
    File_Reader()

main()