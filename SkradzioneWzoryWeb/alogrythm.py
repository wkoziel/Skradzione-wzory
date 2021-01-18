from io import BytesIO
from re import findall, match
from PIL import Image
from sympy import preview
import imagehash
import requests

def cut_out_math(data):
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

def create_list_of_hashes(math):
    """Tworzy hashe z wczytywanego pliku"""
    math_hash = []
    for i in math:
        print("Przetwarzane: "+i)
        byteImgIO = BytesIO()
        preview(r'$$' + i + '$$', output='png', viewer='BytesIO', outputbuffer=byteImgIO, packages=("polski", "inputenc"), euler=False)
        img = Image.open(byteImgIO)
        hash = imagehash.average_hash(img)
        math_hash.append(hash)
    return math_hash

def get_file_from_database(path):
    """Zamienia zdjęcie z bazy na hash"""
    base = "http://skradzionewzory.pythonanywhere.com/static/database/"
    url = base + path
    print("Otwieram:"+url)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    hash = imagehash.average_hash(img)
    return hash

def get_hashes_for_file(dir):
    """Wywołuje pobranie hashu dla każdego pliku z folderu"""
    hash_db = []
    for i in range(1,10):
        file = str(i)+".png"
        hash_db.append([dir+"/"+file, get_file_from_database(dir+"/"+file)])
    return hash_db

def compare_hashes(loaded_file_data):
    """Metoda porównująca zawartość bazy i plik źródłowy"""
    #Zestaw folderów z bazy danych
    files = []
    for i in range(1,51):
        files.append("ex"+str(i))

    base = "http://skradzionewzory.pythonanywhere.com/static/database/"

    results = []
    for file in files:
        math_to_compare = get_hashes_for_file(file)
        match_data = []
        matches = 0
        for i in loaded_file_data:

            for j in math_to_compare:
                diff = i[1] - j[1]
                if diff < 8:
                    matches += 1
                    sim = 100 - 2 * diff
                    match_data.append([i[0], base+j[0], sim])
                    break
        is_enaugh = len(loaded_file_data) / 2
        if match_data and matches > is_enaugh:
            similarity = int(matches / len(loaded_file_data) * 100)
            results.append([file, match_data, similarity])
    return results


def get_file_math(data):
    return cut_out_math(data)

def get_file_hash(data):
    math = cut_out_math(data)
    return create_list_of_hashes(math)

def get_loaded_file_data(data):
    loaded_file_data = []
    math = cut_out_math(data)
    math_hash = create_list_of_hashes(math)
    for i, j in zip(math, math_hash):
        loaded_file_data.append([i, j])
    return loaded_file_data

def alghoritm(data):
    loaded_file_data = get_loaded_file_data(data)
    results = compare_hashes(loaded_file_data)
    return results
