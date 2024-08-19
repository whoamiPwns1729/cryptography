#!/usr/bin/python3
key = "DECKFMYIQJRWTZPXGNABUSOLVH"
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

flag = []
for i in "xqcpCBM":
    if i.islower():
        flag.append(string[key.index(i.upper())].lower())
    else:
        flag.append(string[key.index(i)])

flag.append('{')
for i in "5UE5717U710Z":
    if i.isnumeric():
        flag.append(i)
    else:
        flag.append(string[key.index(i)])

flag.append('_')
for i in "3S0WU710Z":
    if i.isnumeric():
        flag.append(i)
    else:
        flag.append(string[key.index(i)])

flag.append('_')
for i in "59533D2F":
    if i.isnumeric():
        flag.append(i)
    else:
        flag.append(string[key.index(i)])

flag.append('}')
print(f"\n[*] flag : {''.join(flag)}\n")
