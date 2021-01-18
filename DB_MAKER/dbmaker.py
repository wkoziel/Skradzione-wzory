from sympy import *
from PIL import Image, ImageChops
import os, imagehash
from re import findall
from io import BytesIO

#Przed włączeniem programu trzeba opróżnić folder database

def main():
    def separate_formulas(data):
        """Wycina wzory z pliku"""
        data = " ".join(data.split())
        math = []
        list = findall(r"\$\$(.+?)\$\$", data)
        math.extend(list)
        list = findall(r"\\\[(.+?)\\\]", data)
        math.extend(list)
        list = findall(r"\\\((.+?)\\\)", data)
        math.extend(list)
        list = findall(r"\\begin\{displaymath\}(.+?)\\end\{displaymath\}", data)
        math.extend(list)
        list = findall(r"\\begin\{math\}(.+?)\\end\{math\}", data)
        math.extend(list)
        list = findall(r"\\begin\{equation\}(.+?)\\end\{equation\}", data)
        math.extend(list)
        list = findall(r"\\begin\{equation\*\}(.+?)\\end\{equation\*\}", data)
        math.extend(list)
        list = findall(r"\\begin\{eqnarray\}(.+?)\\end\{eqnarray\}", data)
        math.extend(list)
        list = findall(r"\\begin\{eqnarray\*\}(.+?)\\end\{eqnarray\*\}", data)
        math.extend(list)
        list = findall(r"\\begin\{align\}(.+?)\\end\{align\}", data)
        math.extend(list)
        list = findall(r"\\begin\{align\*\}(.+?)\\end\{align\*\}", data)
        math.extend(list)
        list = findall(r"\\begin\{multline\}(.+?)\\end\{multline\}", data)
        math.extend(list)
        list = findall(r"\\begin\{multline\*\}(.+?)\\end\{multline\*\}", data)
        math.extend(list)
        list = findall(r"\\begin\{gather\}(.+?)\\end\{gather\}", data)
        math.extend(list)
        list = findall(r"\\begin\{gather\*\}(.+?)\\end\{gather\*\}", data)
        math.extend(list)
        list = findall(r"\$([^$]*)\$", data)
        list = [elem for elem in list if elem != ""]
        math.extend(list)
        for i in range(len(math)):
                math[i] = math[i].replace('&', '')
        return math


    tex_names = os.listdir('files')
    for name in tex_names:
        f = open("files/" + name, encoding="utf8")
        math = separate_formulas(f.read())
        name = name.replace(".tex", "")
        os.mkdir("database/"+name)
        j = 1
        for i in math:
            print(i)
            preview("$$"+i+"$$", viewer='file', filename="database/"+ name + "/" + str(j) + '.png', packages=("polski", "inputenc"), euler=False)
            j+=1

main()