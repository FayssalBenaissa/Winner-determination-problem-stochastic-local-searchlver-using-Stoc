import random
from random import randint
import time 
def readfile(path):
    file=open(path,'r')
    data=file.readlines()
    achteurs=[]
    b = 0
    for line in data:
        if b==0:
            temp=line.split(" ")
            nbrItem=int(temp[0])
            nbroffre=int(temp[0])
            b=1
        else:
            temp = line.split(" ")
            achteur= (nbrItem+1) * [0]
            for i in range(len(temp)):
                if i == 0:
                    achteur[0]=float(temp[0])
                else : 
                    achteur[int(temp[i])] = 1 
            
            achteurs.append(achteur)
    return achteurs,nbrItem,nbroffre
def generatesolution(A,dict,nbroffre,nbritem,achteurs):
    b=0
    for i in range(nbroffre):
        if b == 0:
            A[dict[i][0]]=1
            b=1
        else:
            if valid(A,achteurs[dict[i][0]],achteurs,nbritem) == 1 :
                
                A[dict[i][0]]=1
       
    return A
    
def valid (Sref,achteur,achteurs,nbritem):
        list_valid=[0]*(nbritem+1)
        index = [i for i , x in enumerate(Sref) if x == 1]
        
        for j in index:
            list_valid = [a + b for a,b in zip(achteurs[j] , achteur)]
        valid = len([i for i in list_valid[1:] if i > 1])
        if valid == 0 :
            return 1
        else :
            return -1
            
def creategraph(achteurs,nbitem):
    graphe={}
    for i in range(nbitem):
        graphe[i]=[]
    for i  in range(nbitem):
        
        for j in range(i+1,nbitem):
            list_valid = [a + b for a,b in zip(achteurs[j] , achteurs[i])]
            valid = len([i for i in list_valid[1:] if i > 1])
            if valid != 0 :
                graphe[i].append(j)
                graphe[j].append(i)
    return graphe     

    
def best(achteurs,nbroffer):
    bestoffer=achteurs[0][0]
    best=0
    for i in range(1,nbroffer):
        if (achteurs[i][0] > bestoffer):
            best=i
            bestoffer=achteurs[i][0]
    return best
   
def cout(A,achteurs):
    list_valid=[0]*(nbritem+1)
    index = [i for i , x in enumerate(A) if x == 1]
        
    for j in index:
        list_valid = [a + b for a,b in zip(achteurs[j] , list_valid)]
    return list_valid[0] 

    
def elenver(A,graphe,bid,nbroffre):
    
    for j in range(nbroffre) :
        if j in graphe[bid] :
            A[j]=0
        else:
             A[j]=1
    return A
    
def enlever(A,bid,achteurs,nbroffre):
        index = [i for i , x in enumerate(A) if x == 1]
        
        for j in range(nbroffre):
            if j != bid:    
                list_valid = [a + b for a,b in zip(achteurs[j] , achteurs[bid])]
                valid = len([i for i in list_valid[1:] if i > 1])
                if (valid!=0):
                    A[j]=0
                
        return A

def getcopy(A):
    s=[]
    for i in A:
     s.append(i)
    return s
        
#Mainnn 
print(" donner un nombre reele entre 0 et 1")
wp=float(input())
print("donne le max iteration")
maxiter=int(input())
start_time = time.time()
path='C:/Users/GCBµ/Downloads/in607'

achteurs,nbritem,nbroffre=readfile(path)
dict={}
A = [0]*nbroffre
for i in range(nbroffre) : 
    r=random.random()
    dict.update({i:r})
    
dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

A=generatesolution(A,dict,nbroffre,nbritem,achteurs)
valid = len([i for i in A[0:] if i == 1])
#graphe=creategraph(achteurs,nbroffre)
#print(valid)
#bestcost=cout(A,achteurs)
#print("le cout de la solution innitial",bestcost)
i=0
b=0
while i< maxiter:
    r=random.random()
    if(r<wp):
        bid= randint(0,nbroffre-1)
    else:
        bid=best(achteurs,nbroffre)
    A[bid]=1
    A=  enlever(A,bid,achteurs,nbroffre)
    
    if(b==0):
        bestcost=cout(A,achteurs)
        meilleursolution=getcopy(A)
        b=1
    else:
        cost=cout(A,achteurs)
        if(cost>bestcost):
            bestcost=cost
            meilleursolution=getcopy(A)
    #print("ouss")
    i+=1


print("--- le temps d'execution est :%s seconds ---" % (time.time() - start_time))
print("le meilleur cout",bestcost)
#print(meilleursolution)
print("afficher les gagnants : ")
index = [i for i , x in enumerate(meilleursolution) if x == 1]
for i in index:
    print("l'offre numéro "+str(i+1)+" est acceptée")
print("--- %s seconds ---" % (time.time() - start_time))







