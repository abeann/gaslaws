import re
import util

def boyle(given):
    given = given.split()
    p = []
    v = []
    for i in range(3):
        if re.search("mL", given[i]):
            given[i] = util.mLL(given[i])
        if re.search("atm", given[i]):
            p.append(float(given[i].replace("atm", "")))
        else:
            v.append(float(given[i].replace("L", "")))
    if len(p) == 2:
        V = (p[0] * v[0]) / p[1]
        return f"Volume = {round(V, util.R)}L"
    else:
        P = (p[0] * v[0]) / v[1]
        return f"Pressure = {round(P, util.R)}{util.pt}"

def charles(given):
    given = given.split()
    v = []
    t = []
    for i in range(3):
        if re.search("mL", given[i]):
            given[i] = util.mLL(given[i])
        if re.search("C", given[i]):
            given[i] = util.CK(given[i])
        if re.search("K", given[i]):
            t.append(float(given[i].replace("K", "")))
        else:
            v.append(float(given[i].replace("L","")))
    if len(t) == 2:
        V = (v[0] * t[1]) / t[0]
        return f"Volume = {round(V, util.R)}L"
    else:
        T = (t[0] * v[1]) / v[0]
        return f"Temperature = {round(T, util.R)}K or {round(T - 273, util.R)}C"
    
def gaylussac(given):
    given = given.split()
    p = []
    t = []
    for i in range(3):
        if re.search("C", given[i]):
            given[i] = util.CK(given[i]) 
        if re.search ("atm", given[i]):
            p.append(float(given[i].replace("atm", "")))
        else:
            t.append(float(given[i].replace("K", "")))
    if len(p) == 2:
        T = (t[0] * p[1]) / p[0]
        return f"Temperature = {round(T, util.R)}K or {round(T - 273, util.R)}C"
    else: 
        P = (p[0] * t[1]) / t[0]
        return f"Pressure = {round(P, util.R)}{util.pt}"

def combined(given):
    given = given.split()
    p = []
    v = []
    t = []
    for i in range(5):
        if re.search("C", given[i]):
            given[i] = util.CK(given[i])
        if re.search("mL", given[i]):
            given[i] = util.mLL(given[i])
        if re.search("atm", given[i]):
            p.append(float(given[i].replace("atm", "")))
        elif re.search("L", given[i]):
            v.append(float(given[i].replace("L", "")))
        else:
            t.append(float(given[i].replace("K", "")))
    if len(v) == 2 and len(t) == 2:
        P = (p[0] * v[0] * t[1]) / (v[1] * t[0])
        return f"Pressure = {round(P, util.R)}{util.pt}"
    elif len(p) == 2 and len(t) == 2:
        V = (p[0] * v[0] * t[1]) / (p[1] * t[0])
        return f"Volume = {round(V, util.R)}L"
    else:
        T = (p[1] * v[1] * t[0]) / (p[0] * v[0])
        return f"Temperature = {round(T, util.R)}K or {round(T - 273, util.R)}C"