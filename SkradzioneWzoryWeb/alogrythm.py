from io import BytesIO
from re import findall
from PIL import Image
from sympy import preview
import imagehash

def cut_out_math(data):
    data = " ".join(data.split())
    #data = data.replace(" ", "")
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
    math_hash = []
    for i in math:
        print("Przetwarzane: "+i)
        byteImgIO = BytesIO()
        preview(r'$$' + i + '$$', output='png', viewer='BytesIO', outputbuffer=byteImgIO)
        img = Image.open(byteImgIO)
        #UWAGA! OTWIERANIE OBRAZÓW PRZEZ APLIKACJE LINIJKA NIŻEJ
        #img.show()
        hash = imagehash.average_hash(img)
        print(hash.__repr__)
        math_hash.append(hash)
    return math_hash

def compare_hashes(math_hash):
    #To wgl nie ma narazie sensu, sprawdzam tylko czy działa xd
    result = []
    for i in math_hash:
        for j in math_hash:
            if i != j:
                    cutoff = 10
                    diff = i - j
                    if diff < cutoff:
                        result.append(str(i)+" oraz "+str(j)+" są podobne")

    return result

def get_file_math(data):
    return cut_out_math(data)

def get_file_hash(data):
    math = cut_out_math(data)
    return create_list_of_hashes(math)

def alghoritm(data):
    math = cut_out_math(data)
    math_hash = create_list_of_hashes(math)
    result = compare_hashes(math_hash)
    return result
