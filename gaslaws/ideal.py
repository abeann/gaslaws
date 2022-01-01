import re
import util

def ideal(given):
    if re.search("kPa", given):
        pt = "kPa"
        r = 8.3145
    elif re.search("mmHg", given):
        pt = "mmHg" 
        r = 62.4
    else:
        pt = "atm"
        r = 0.082057
    PV = []
    nT = []
    pressure = False
    volume = False
    mol = False
    Temp = False
    given = given.split()
    for i in range(3):
        if re.search("C", given[i]):
            given[i] = util.CK(given[i])
        if re.search("mL", given[i]):
            given[i] = util.mLL(given[i])
        if re.search(f"{pt}", given[i]):
            PV.append(float(given[i].replace(f"{pt}", "")))
            pressure = True
        elif re.search("L", given[i]):
            PV.append(float(given[i].replace("L", "")))
            volume = True
        elif re.search("mol", given[i]):
            nT.append(float(given[i].replace("mol", "")))
            mol = True
        else:
            nT.append(float(given[i].replace("K", "")))
            Temp = True
    if len(PV) == 1:
        x = (nT[0] * nT[1] * r) / PV[0]
        if pressure == False:
            return f"Pressure = {round(x, util.R)}atm"
        else:
            return f"Volume = {round(x, util.R)}L"
    else:
        x = (PV[0] * PV[1]) / (r * nT[0])
        if mol == False:
            return f"{round(x, util.R)}mol"
        else:
            return f"Temperature = {round(x, util.R)}K or {round(x -273, util.R)}C"