#Diego Roberto Roche Palacios 201603188
#Proyectos980

def pares(N):
    ans1=N/2
    return ans1

def impares(N):
    ans2=3*N+1
    return ans2

archivo=open("collatz.txt","w")

for i in range(2,189,1):
    lista=[i]
    d=i
    while lista[-1]!=1:
        if(d%2==0):
            r=pares(d)
        else:
            r=impares(d)
        d=r
        lista.append(int(r))
    archivo.write(str(lista)+"\n")    


archivo.close()

