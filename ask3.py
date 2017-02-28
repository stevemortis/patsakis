lista=[1,2,5,67,8765,345,65,0,9,0,4367,0,0,0,3,213,0,4,0,56,0,0,456]

i = 0
for num in lista:
    if num == 0:
        i = i +1



lista = list(filter(lambda a: a != 0, lista))

print("Λίστα χωρίς μηδενικά:", lista)

for num in range(0,i):
    lista.append(0)

print("Νέα λίστα:", lista)
