names_a = []
with open('a.txt') as f:
    test = f.read().splitlines()
    names_a.append(test)

names_b = []
with open('b.txt') as f:
    test = f.read().splitlines()
    names_b.append(test)


flatten = lambda l: [item for sublist in l for item in sublist]

final_a = flatten(names_a)
final_a = list(set(final_a))
final_a.sort()

final_b = flatten(names_b)
final_b = list(set(final_b))
final_b.sort()

# a are new AI names, b are existing names from riot api
new_names = [item for item in final_a if item not in final_b]

with open('finalllll.txt', 'w') as f:
    for i in new_names:
        f.write("%s\n" % i)

