def fatorial(número):
    if número==1:
        return 1
    return número*fatorial(int(número-1))

n=int(input())
print(fatorial(n))

