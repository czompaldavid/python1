#Az adott lista ('ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python') elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!

szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
lista = []
for szo in szavak:
  if szo[0] == "t" or szo[0] == "T":
    lista.append(szo)
print(lista)
