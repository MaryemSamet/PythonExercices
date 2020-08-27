import numpy as np


def voisinsCase (plateau, i, j):
    L = []
    
    # enregistrer les voisins libres 
    if i > 0:
        if plateau[i-1][j] == False:
            L.append([i-1,j])
        
    if j > 0 :
        if plateau[i][j-1] == False:
            L.append([i,j-1])
        
 
    if i< len(plateau)-1:  
        if plateau[i+1][j] == False:
            L.append([i+1,j])
        
    if j< len(plateau[i])-1: 
        if plateau[i][j+1] == False:
            L.append([i,j+1])
        
    return L
    
    
    
def voisinsCases(plateau , ensembleCases):
    list_voisins = []
    while (True):
        
        ancien_len = len(list_voisins)
        voisins = []
      
        for i in range(len(ensembleCases)):
            
            if voisinsCase(plateau,ensembleCases[i][0],ensembleCases[i][1]) != []:
                voisins.append( voisinsCase(plateau,ensembleCases[i][0],ensembleCases[i][1]) )
                
        if voisins == [] :
            return list_voisins
        else :
            l1 = voisins[0]
            for i in range(len(l1)):
                if  appartient(l1[i][0],l1[i][1],list_voisins) == False :
                    list_voisins.append(l1[i])
            ensembleCases = []
            for i in range (len(voisins[0])):
                ensembleCases.append(voisins[0][i])
        if len(list_voisins)== ancien_len:
            return(list_voisins)
        
                
        
        
    
def accessibles (plateau,i,j):
    voisin_case_list = voisinsCase(plateau,i,j)
    
    tous_voisins_accessible = voisinsCases(plateau, voisin_case_list)
    print("ce sont tous les voisins",tous_voisins_accessible)
    
    return tous_voisins_accessible
    
def appartient(finI,finJ, L  ):
    for i in range(len(L)):
        if L[i] == [finI,finJ]:
            return True 
    return( False) 
    
def chemin(plateau, debI,debJ, finI,finJ ):
    L = accessibles (plateau, debI,debJ)
    if appartient(finI,finJ, L  ) : 
        return True
    else :
        return False
        




if __name__ == '__main__':

    Plateau= [[True , False , False , False ] ,[False , True , True , False ] ]

    debI = int(input("enter debI "))
    debJ = int(input("enter debJ "))
    finI = int(input("enter finI "))
    finJ = int(input("enter finJ "))
    if chemin(Plateau,debI,debJ,finI,finJ) : 
        print("True")
    else : 
        print("False")


    
    
    
        
    
