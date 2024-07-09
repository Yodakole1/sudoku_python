import random
from sudokuSolver import *



#Generate sudoku puzzle
def generisi_sudoku():
    #Initialize empty board
    tabla = [[0 for _ in range (9)]for _ in range (9)]

    for i in range(0,9,3):
        brojevi = [1,2,3,4,5,6,7,8,9]
        random.shuffle(brojevi)
        for j in range(3):
            for k in range(3):
                tabla[i+j][i+k] = brojevi.pop()

    #Backtracking function 
    provera_resenja_sudoku(tabla)



    #Empty cells
    prazna_mesta = random.randint(20,58)

    #Remove some numbers
    while(prazna_mesta>0):
        vrsta  = random.randint(0, 8)
        kolona = random.randint(0, 8)

        if(tabla[vrsta][kolona] != 0):
            tabla[vrsta][kolona] = 0
            prazna_mesta -= 1


    

    return tabla        

#Copy board for user
def kopiranje_table(tabla):
    kopirana_tabla = [[0 for _ in range (9)]for _ in range (9)]
    for i in range(0,9):
        for j in range(0,9):
            kopirana_tabla[i][j]=tabla[i][j]


    return kopirana_tabla            