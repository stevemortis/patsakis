print("Πληκτρολογηστε αριθμους χωρισμενους με κενα")
lista=[int(x) for x in input().split()]
print("Αρχική Λίστα",lista)
i = 0
for num in lista:
    if num == 0:
        i = i +1



lista = list(filter(lambda a: a != 0, lista))

print("Λίστα χωρίς μηδενικά:", lista)

for num in range(0,i):
    lista.append(0)

print("Νέα λίστα:", lista)
