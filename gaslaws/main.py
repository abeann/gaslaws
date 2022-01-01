import re
import util
from gaslaws import boyle, charles, gaylussac, combined
from ideal import ideal

def main():
    while True:
        given = input("Given: ")
        if given == "end":
            break
        if given == "Rchange":
            util.R = int(input("R = "))

        if re.search("mmHg", given):
                util.pt = "mmHg"
                given = given.replace("mmHg", "atm")
        elif re.search("kPa", given):
            util.pt = "kPa"
            given = given.replace("kPa", "atm")
        elif re.search("atm", given):
            util.pt = "atm"

        if len((given).split()) == 3:
            if re.search("mol", given) or (re.search("L{1}|m{1}L{1}", given) and re.search("atm{1}|kPa{1}|mmHg{1}", given) and re.search("C{1}|K{1}", given)):
                print(ideal(given))
            else:
                if re.search("L|mL", given) and re.search("atm", given):
                    print(boyle(given))
                elif re.search("K|C", given) and re.search("L|mL", given):
                    print(charles(given))
                elif re.search("K|C", given) and re.search("atm", given):
                    print(gaylussac(given))
        elif len((given).split()) == 5:
            given = given.replace("mmHg", "atm")
            given = given.replace("kPa", "atm")
            print(combined(given))

main()