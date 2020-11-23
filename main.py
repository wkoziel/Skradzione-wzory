import os, re

class Files:
    def __init__(self, data, name):
        self.name = name
        self.math = []
        self._prepare_data(data)

    def _prepare_data(self, data):
        data = " ".join(data.split())
        data = data.replace(" ", "")
        self._separate_formulas(data)

    def _separate_formulas(self, data):
        print("Dane dla pliku: "+self.name)
        # self.math.append(re.findall(r"\$(.+?)\$", data)) #$...$
        # self.math.append(re.findall(r"\$\$(.+?)\$\$", data)) #$...$
        self.math.append(re.findall(r"\\\[(.+?)\\\]", data))
        self.math.append(re.findall(r"\\\((.+?)\\\)", data))
        self.math.append(re.findall(r"\\begin\{displaymath\}(.+?)\\end\{displaymath\}", data))
        self.math.append(re.findall(r"\\begin\{math\}(.+?)\\end\{math\}", data))
        self.math.append(re.findall(r"\\begin\{equation\}(.+?)\\end\{equation\}", data))
        self.math.append(re.findall(r"\\begin\{equation\*\}(.+?)\\end\{equation\*\}", data))
        self.math.append(re.findall(r"\\begin\{eqnarray\}(.+?)\\end\{eqnarray\}", data))
        self.math.append(re.findall(r"\\begin\{eqnarray\*\}(.+?)\\end\{eqnarray\*\}", data))
        self.math.append(re.findall(r"\\begin\{align\}(.+?)\\end\{align\}", data))
        self.math.append(re.findall(r"\\begin\{align\*\}(.+?)\\end\{align\*\}", data))
        self.math.append(re.findall(r"\\begin\{multline\}(.+?)\\end\{multline\}", data))
        self.math.append(re.findall(r"\\begin\{multline\*\}(.+?)\\end\{multline\*\}", data))
        self.math.append(re.findall(r"\\begin\{gather\}(.+?)\\end\{gather\}", data))
        self.math.append(re.findall(r"\\begin\{gather\*\}(.+?)\\end\{gather\*\}", data))
        self.math = [x for x in self.math if x != []] #usuwa puste
        print(self.math)
        print(" ")

class File_Reader:

    def __init__(self):
        self.files = []
        self.files_names = []
        self._names_download()
        self._read_file()

    def _names_download(self):
        self.files_names = os.listdir('database')


    def _read_file(self):
        print("Wczytywanie plików: "+str(self.files_names)+"\n")
        for file in self.files_names:
            f = open("database/" + file,"r")
            self.files.append(Files(f.read(), str(file)))


def main():
    File_Reader()

main()