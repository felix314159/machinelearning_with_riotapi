names = []
with open('output_cleaned.txt') as f:
    test = f.read().splitlines()
    names.append(test)


flatten = lambda l: [item for sublist in l for item in sublist]

final = flatten(names)
final = list(set(final))
final.sort()


with open('output_sorted.txt', 'w') as f:
    for i in final:
        f.write("%s\n" % i)

