from random import uniform
from math import pi

n=int(input("Quantos pontos queres?"))
contador=0

for i in range(0,n+1):   
    x=uniform(-1,1)
    y=uniform(-1,1)
    if x**2+y**2<=1:
        contador+=1

print("pi=",4*contador/n)
print("desvio",(4*contador/n-pi)*100/pi)

