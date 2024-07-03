import random




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
    prazna_mesta = 46

    

    #Remove some numbers
    while(prazna_mesta>0):
        vrsta  = random.randint(0, 8)
        kolona = random.randint(0, 8)

        if(tabla[vrsta][kolona] != 0):
            tabla[vrsta][kolona] = 0
            prazna_mesta -= 1

        
    return tabla        




def pronadji_prazna_polja(tabla):
    for i in range(9):
        for j in range(9):
            if(tabla[i][j] == 0):
                return i,j
            
    return -1,-1            


def provera_resenja_sudoku(tabla):
    #Find empty cell
    vrsta,kolona = pronadji_prazna_polja(tabla)

    #Puzzle is solved
    if(vrsta == -1):
        return True 
    
    for broj in range(1,10):
        if(validan_potez(tabla,vrsta,kolona,broj)):
            #Place num
            tabla[vrsta][kolona] = broj

            #Recursion
            if(provera_resenja_sudoku(tabla)):
                return True
        
        #If not possible remove that number
        tabla[vrsta][kolona] = 0

    #Backtrack
    return False        



def validan_potez(tabla,vrsta,kolona,broj):
    
    #Check if num is in row
    for i in range(0,9):
        if(tabla[vrsta][i] == broj):
            return False
        
    #Check if num is in column
    for i in range(0,9):
        if(tabla[i][kolona] == broj):
            return False
        

    vrsta_kvadrata = (vrsta // 3) * 3
    kolona_kvadrata = (kolona // 3) * 3

    for i in range(vrsta_kvadrata,vrsta_kvadrata+3):
        for j in range(kolona_kvadrata,kolona_kvadrata+3):
            if(tabla[i][j] == broj):
                return False

    return True

def print_a(tabla):
    for i in tabla:
        print(i)


tabla = generisi_sudoku()
print_a(tabla)

print("","\n")

if(provera_resenja_sudoku(tabla)):
    print_a(tabla)  
else:
    print("danedoa")       