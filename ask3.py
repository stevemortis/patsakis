print("Dwste ari8mous xwrismenous me kena")
lista=[int(x) for x in input().split()]
print("Arxikh Lista",lista)
i = 0
for num in lista:
    if num == 0:
        i = i +1



lista = list(filter(lambda a: a != 0, lista))

print("Lista xwris mhdenika:", lista)

for num in range(0,i):
    lista.append(0)

print("Nea lista:", lista)
