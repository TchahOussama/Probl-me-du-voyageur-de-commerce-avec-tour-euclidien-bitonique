from itertools import*

import timeit
def bitonique_iter(N):
    start = timeit.default_timer()

    ####exemple##############
    table = {i:{} for i in range(1,N)}
    poid = {}
    for i in range(1,len(table)+1):
        for j in range(1,len(table)+1):
            if i!=j:
                poid[(i,j)] = i*j

    ## FIN EXEMPLE 

    chemin_depart = {}
    for i in range (0,len(table)-1):
        for j in range(2,len(table)):
            ### traitement des cas speciales
            if i ==0:
                name = (len(table),1)
                chemin_depart[name] = poid[(len(table),1)]
                break
            if i ==1:
                name = (len(table),j,1)
                chemin_depart[name] = poid[(j,1)] + poid[(len(table),j)]
            ### main loop:
            # this part crates roads between 1 and len(table) and in between them it puts a number of points equalts to i for example
            # --- a road with i=4 is (1-3-4-6-7-9) or (1-2-3-4-5-9) ... (there is 4 numbers between 1 and len(table))
            # with this methode we can go through all the possible roads beetween 1 and len(table).   
            else :
                combination = list(combinations([i for i in range(2,len(table))],i))
                for item in combination:
                    abc = list(item)
                    abc.reverse()
                    value = 0
                    #print(item)
                    #input()
                    chemin = [len(table)]+abc+[1]
                    for point in range (0,len(chemin)-1):
                        value = value + poid[(chemin[point],chemin[point+1])]
                    name = tuple(chemin)
                    chemin_depart[name] = value
            #print(chemin_depart)
            #input() 
        
    bitonique = chemin_depart

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
        #print(name)
        #print(chemin_value)
        if counter==0:
            best_chemin = name
            best_value = chemin_value
        if chemin_value<best_value:
            best_chemin = name
            best_value = chemin_value
            ################ if theres is a lot of routes who have the same value (case untreated)
        counter+= 1
    #print('---------------------------------------------------------------------')    
    #print('The best route is : '+ str(best_chemin))
    #print('His value is :' + str(best_value))      

    stop = timeit.default_timer()

    #print('Time: ', stop - start)  
    return stop-start
if __name__ == "__main__":
    bitonique_iter(20)


