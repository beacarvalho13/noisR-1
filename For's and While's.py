valor_monetário= int(input())

notas=[500,200,100,50,20,10,5,2,1]
números=[]

for x in notas:
    número=int(valor_monetário//x)
    valor_monetário=int(valor_monetário-x*número)
    números.append(número)

for i in range(0,10):
    if números[i]!=0:
        print(notas[i],"->",números[i])
