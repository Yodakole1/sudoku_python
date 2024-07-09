#Find cells
def pronadji_prazna_polja(tabla):
    
    for i in range(9):
        for j in range(9):
            if(tabla[i][j] == 0):
                return i,j
            
    
    return -1,-1            


#Check solution
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


#Valid move
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