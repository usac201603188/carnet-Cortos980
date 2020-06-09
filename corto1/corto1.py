#Diego Roberto Roche Palacios 201603188
#Proyectos980

def pares(N):
    ans1=N/2
    return ans1

def impares(N):
    ans2=3*N+1
    return ans2

archivo=open("corto1/collatz.txt","w")

for i in range(2,189,1):    #Todo dentro de una lista para que ejecute cada secuencia en una linea diferente
    lista=[i]
    d=i                      #para no afectar la i que se está leyendo agrego una variable que servirá despues
    while lista[-1]!=1:
        if(d%2==0):         #Evaluacion si son pares o impares
            r=pares(d)
        else:
            r=impares(d)
        d=r                 #igualo mi variable al resultado obtenido 
        lista.append(int(r))
    archivo.write(str(lista)+"\n")    #Escritura del archivo 


archivo.close()

