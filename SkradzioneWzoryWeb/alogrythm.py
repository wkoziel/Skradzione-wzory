from re import findall

def cut_out_math(data):
    data = " ".join(data.split())
    data = data.replace(" ", "")
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
    return math

def alghoritm(data):
    return cut_out_math(data)
