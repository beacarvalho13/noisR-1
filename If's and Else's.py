frase = input()

lista= frase.split(" ")

for x in range(len(lista)): 
    lista[x]=int(lista[x])

    
def triângulo(a,b,c):
    if a<b+c and b<a+c and c<b+a:
        return True
    else:
        return False

result=triângulo(lista[0],lista[1],lista[2])

if result:
    if lista[0]==lista[1]==lista[2]:
        print("Sim, é um triângulo equilátero.")
    elif lista[0]==lista[1] or lista[0]==lista[2] or lista[1]==lista[2]:
        print("Sim, é um triângulo isósceles.")
    else:
        print("Sim, é um triângulo escaleno.")
else:
    print("Não é triângulo.")
    