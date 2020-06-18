####exemple##############
table = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{}}
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