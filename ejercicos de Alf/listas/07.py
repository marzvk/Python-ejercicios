abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

for i in range(len(abecedario), 0, -1):
    if i % 3 == 0:
        abecedario.pop(i - 1)
    print(i, abecedario[i - 1])
print(abecedario)
