import pandas as pd


def check_string(string):
    if all(x.isalnum() or x.isspace() for x in string) and string.isascii():
        return True

    else:
        return False


data = pd.read_json("test.json")
test = data["players"]

names = []
for i in test:
    names.append(i["name"])
    
names.sort()

with open('master_names_clean.txt', 'w') as f:
    for i in names:
        if check_string(i):
            f.write("%s\n" % i)