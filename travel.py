nodes = int(input("Enter number of cities: "))
g = []
d = {}
va = {}

for i in range(nodes):
    node = []
    valu = []
    n = int(input("Enter the particular city: "))
    a = int(input("Enter the number of adjacents for the given city: "))

    for j in range(a):
        b = int(input("Enter the adjacent city: "))
        v = int(input("Enter the adjacent city value: "))
        node.append(b)
        valu.append(v)

    d[n] = node
    va[n] = valu

start = int(input("Enter the start node or city: "))
final = []
finalvalue = []
g.append(start)


def find(start, final, g):
    flag = False

    for j in d[start]:
        if j not in g:
            g.append(j)
            flag = True

            final, g = find(j, final, g)

            # If the path is valid, append it to 'final'
            if len(g) == nodes:
                final.append(g[:])

            g.pop()  # Remove the last node when backtracking

    return final, g


final, g = find(start, final, g)

for i in final:
    sum = 0
    for j in range(len(i) - 1):
        if i[j] in d and i[j + 1] in d[i[j]]:
            k = d[i[j]].index(i[j + 1])
            sum += va[i[j]][k]
        else:
            print(f"Key {i[j]} or {i[j + 1]} not found in dictionary")

    finalvalue.append(sum)

if finalvalue:  # Check if finalvalue is not empty
    m = min(finalvalue)
else:
    print("Final value is empty")
    m = None

if m is not None:
    print("Optimum path:")
    for i in range(0, len(finalvalue)):
        if finalvalue[i] == m:
            print(final[i], 'Total path cost', m)

print("Total paths:", len(final))
for i in range(0, len(final)):
    print(i + 1, '.', final[i],'->', 'Total path cost', finalvalue[i])