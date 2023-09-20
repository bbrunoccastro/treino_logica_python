def bubble_sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        while i < fim - 1:
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
            i += 1
        fim -= 1
    return v


listaNumeros = list()
for c in range(1, 4):
    listaNumeros.append(int(input(f'Digite o {c}º valor: ')))

print(bubble_sort(listaNumeros))
