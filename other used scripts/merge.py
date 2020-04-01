yo = []

with open('flex_bronze_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)
    
with open('flex_diamond_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('flex_gold_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)


with open('flex_iron_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)
    
with open('flex_master_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('flex_plat_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('flex_silver_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)
    
with open('solo_bronze_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('solo_diamond_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('solo_gold_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)
    
with open('solo_iron_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('solo_platinum_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)

with open('solo_silver_names_clean.txt') as f:
    test = f.read().splitlines()
    yo.append(test)
    
with open('z_masters_na_eu_asia.txt') as f:
    test = f.read().splitlines()
    yo.append(test)


flatten = lambda l: [item for sublist in l for item in sublist]

final = flatten(yo)
final = list(set(final))
final.sort()


with open('final.txt', 'w') as f:
    for i in final:
        f.write("%s\n" % i)

