global R
global pt

R = 3

pt = ""

def CK(n):
    n = n.replace("C", "")
    n = str(int(n) + 273)
    n += "K"
    return n

def mLL(n):
    n = n.replace("mL", "")
    n = str(int(n) / 1000)
    n += "L"
    return n

