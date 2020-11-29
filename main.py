import os, re

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

        self._print_stats(data)

    def _print_stats(self, data):
        """Szybkie dane dla szukania błędów i testowania"""
        #print("\nDANE Z PLIKU: "+self.name+"\n"+data) #Print nazyw i tekstu z plików
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


def main():
    reader = File_Reader()
main()