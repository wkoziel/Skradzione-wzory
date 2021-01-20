from io import BytesIO
from re import findall, match
from PIL import Image
from sympy import preview
import imagehash
import requests
import time

def cut_out_math(data):
    """Oczyszcza plik z problematycznych znaków i zwraca listę wzorów zawartych w pliku"""

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

def create_list_of_hashes(math):
    """Dla zadanej listy wzorów zwraca listę hashy wygenerowanych na podstwie graficznej reprezentacji wzoru"""

    math_hash = []
    for i in math:
        print("Przetwarzanie wzory:"+i)
        byteImgIO = BytesIO()
        preview(r'$$' + i + '$$', output='png', viewer='BytesIO', outputbuffer=byteImgIO, packages=("polski", "inputenc"), euler=False)
        img = Image.open(byteImgIO)
        hash = imagehash.average_hash(img)
        math_hash.append(hash)
    return math_hash

def get_file_from_database(path):
    """Pobiera graficzną reprezentacje wzoru i zwraca jego hash"""

    #base = "http://skradzionewzory.pythonanywhere.com/static/database/"
    base = "http://127.0.0.1:8000/static/database/"
    response = requests.get(base + path)
    img = Image.open(BytesIO(response.content))
    hash = imagehash.average_hash(img)
    return hash

def get_hashes_for_file(dir):
    """Wywołuje pobranie hashu dla każdego pliku z folderu"""

    hash_db = []
    for i in range(1,11):
        file = str(i)+".png"
        hash_db.append([dir+"/"+file, get_file_from_database(dir+"/"+file)])
    return hash_db

def compare_hashes(loaded_file_data):
    """Metoda porównująca zawartość bazy i plik źródłowy"""

    #Zestaw folderów z bazy danych
    files = []
    for i in range(1,51):
        files.append("ex"+str(i))

    #base = "http://skradzionewzory.pythonanywhere.com/static/database/"
    base = "http://127.0.0.1:8000/static/database/"

    results = []
    for file in files:
        #Pętla przeszukuje baze danych ex1, ex2, ex3
        math_to_compare = get_hashes_for_file(file)
        match_data = []
        matches = 0
        for wzor1 in loaded_file_data:
            #Pętla przeszukuje wzory zadane w pliku
            tmp_diff_num = []
            tmp_match_data = []
            for wzor2 in math_to_compare:
                #Pętla przeszukuje wzory zadane w bazie dla aktualnego exX
                diff = wzor1[1] - wzor2[1]
                if diff < 9:
                    sim = int(((64 - diff) / 64) * 100)
                    tmp_diff_num.append(diff)
                    tmp_match_data.append([wzor1[0], base+wzor2[0], sim])
            min = -1
            if tmp_match_data:
                matches += 1
                index = 0
                min = tmp_diff_num[0]
                for i in range(0, len(tmp_diff_num)):
                    if min > tmp_diff_num[i]:
                        index = i
                        min = tmp_diff_num[i]

                match_data.append(tmp_match_data[index])

        is_enaugh = len(loaded_file_data) * 0.7
        if match_data and matches > is_enaugh:
            similarity = int(matches / len(loaded_file_data) * 100)
            results.append([file, match_data, similarity])

    return results


def get_file_math(data):
    """Zwraca listę wzorów z zadanego pliku"""

    return cut_out_math(data)

def get_file_hash(data):
    """Zwraca liste hashy z zadanego pliku"""

    math = cut_out_math(data)
    return create_list_of_hashes(math)

def get_loaded_file_data(data):
    """Przetwarza zadany plik by uzyskać listę wzoró oraz ich hashy"""

    loaded_file_data = []
    math = cut_out_math(data)
    math_hash = create_list_of_hashes(math)
    for i, j in zip(math, math_hash):
        loaded_file_data.append([i, j])
    return loaded_file_data

def alghoritm(data):
    """Główny algorytm kontolujący etapy postępowania programu"""

    start = time.time()
    loaded_file_data = get_loaded_file_data(data)
    results = compare_hashes(loaded_file_data)
    end = time.time()
    print("Wykonanie algorytmu zajęło: "+str(end - start)+" sekund.")
    return results
