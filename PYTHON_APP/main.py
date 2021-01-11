from sympy import *
from PIL import Image, ImageChops
import os, re, imagehash

class Files:

    def __init__(self, data, name):
        """Tworzy obiekt pliku zawierający nazwę i listę wzorów"""
        self.name = name
        self.math = []
        self._prepare_data(data)

    def _prepare_data(self, data):
        """Usuwa wszystkie znaki białe i zmienia tekst w jeden ciąg"""
        data = " ".join(data.split())
        data = data.replace(" ", "")
        self._separate_formulas(data)

    def _separate_formulas(self, data):
        """Wyszukuje wzory pomiędzy zadanymi komendami i zapisuje w liście jednowymiarowej math"""
        list = re.findall(r"\$\$(.+?)\$\$", data)
        self.math.extend(list)
        list = re.findall(r"\\\[(.+?)\\\]", data)
        self.math.extend(list)
        list = re.findall(r"\\\((.+?)\\\)", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{displaymath\}(.+?)\\end\{displaymath\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{math\}(.+?)\\end\{math\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{equation\}(.+?)\\end\{equation\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{equation\*\}(.+?)\\end\{equation\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{eqnarray\}(.+?)\\end\{eqnarray\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{eqnarray\*\}(.+?)\\end\{eqnarray\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{align\}(.+?)\\end\{align\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{align\*\}(.+?)\\end\{align\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{multline\}(.+?)\\end\{multline\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{multline\*\}(.+?)\\end\{multline\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{gather\}(.+?)\\end\{gather\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{gather\*\}(.+?)\\end\{gather\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\$([^$]*)\$", data)
        list = [elem for elem in list if elem != ""]
        self.math.extend(list)

        for i in range(len(self.math)):
            self.math[i] = self.math[i].replace('&', '')

        #self._print_stats(data)

    def _print_stats(self, data):
        """Szybkie dane dla szukania błędów i testowania"""
        print("\nDANE Z PLIKU: "+self.name+"\n"+data) #Print nazyw i tekstu z plików
        print("\nWZORY:"+str(self.math)) #Print listy z wzorami


class File_Reader:

    def __init__(self):
        """Wywołuje wczytywanie plików z /database i przechowuje tablice sprawdzonych plików"""
        self.files = []
        self._read_file()

    def _names_download(self):
        """Zwraca nazwy plików znajdujących się w /database"""
        return os.listdir('database')

    def _read_file(self):
        """Zwraca nazwy plików znajdujących się w /database"""
        file_names = self._names_download()
        for file in file_names:
            f = open("database/" + file,"r")
            self.files.append(Files(f.read(), file))

    def compare(path1, path2):
        img1 = Image.open(path1)
        img2 = Image.open(path2)

        hash0 = imagehash.average_hash(img1)
        hash1 = imagehash.average_hash(img2)

        max_diff = 10
        diff = hash0 - hash1

        if diff < max_diff:
            print('Wzory SĄ podobne')
            return True
        else:
            print('Wzory NIE są podobne')
            return False

def make_img(exp, f, i):
    f = f.replace(".tex", 'wzor')
    print("robie obrazek"+ str(f) + str(i) + '.png')
    preview(exp, viewer='file', filename='images/test' + str(f) + str(i) + '.png')

def image_making_loop(reader):
    for x in range(len(reader.files)):
            for i in range (len(reader.files[x].math)):
                print(reader.files[x].math[i])
                #make_img(r'$$' + reader.files[x].math[i] + '$$', reader.files[x].name, i)

def main():
    reader = File_Reader()
    #image_making_loop(reader)


main()