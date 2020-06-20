####exemple##############
table = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}
poid = {}
for i in range(1,len(table)+1):
    for j in range(1,len(table)+1):
        if i!=j:
            poid[(i,j)] = i/j

print(poid)
## FIN EXEMPLE 

## THE DYNAMIC PART
for i in range (2,len(table)+1):
    table[i][(i,1)] = poid[i,1]
    #print('i = ' + str(i))
    #input()
    for j in range (i-1,1,-1):
        #print('j = '+ str(j))
        #input()
        for key, value in table[j].items():
            name = [i] + list(key)
            index = tuple(name)
            table[i][index] = poid[i,j]+value

bitonique = table[len(table)]
best_chemin = []
counter = 0
for key, value in bitonique.items():
    chemin_depart = list(key)
    chemin_retour = [len(table)]
    for i in range (len(table),1,-1):
        if i not in chemin_depart:
            chemin_retour.append(i)
    chemin_retour.append(1)
    chemin_depart.reverse()        
    chemin_value = value + bitonique[tuple(chemin_retour)]
    chemin_retour.pop(0)
    name =chemin_depart  + chemin_retour
    print(name)
    print(chemin_value)
    if counter==0:
        best_chemin = name
        best_value = chemin_value
    if chemin_value<best_value:
        best_chemin = name
        best_value = chemin_value
        ################ if theres is a lot of routes who have the same value (case untreated)
    counter+= 1
print('---------------------------------------------------------------------')    
print('The best route is : '+ str(best_chemin))
print('His value is :' + str(best_value))