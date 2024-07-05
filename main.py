import pygame
from sudokuGenerator import *
from sudokuSolver import *



#Constants
WINDOW_SIZE = 600
CELL_SIZE = WINDOW_SIZE // 9
GRID_SIZE = CELL_SIZE * 9
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
HIGHLIGHT_COLOR = (180, 180, 255)
TEXT_COLOR = (0, 0, 0)
LOCKED_TEXT_COLOR = (200, 0, 0)
BUTTON_COLOR = (0, 150, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

#Initialize pygame
pygame.init()


#Display
screen = pygame.display.set_mode((WINDOW_SIZE-5, WINDOW_SIZE + 80))
pygame.display.set_caption("Sudoku")


#Font
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 28)
message_font = pygame.font.Font(None, 48)



#Draw grid
def nacrtaj_grid():
    for i in range(10):
        width = 1 if i % 3 != 0 else 3
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_SIZE), width)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (GRID_SIZE, i * CELL_SIZE), width)




#Printing numbers in GUI
def ispis_brojeva(board, zakljucane_celije):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text_color = LOCKED_TEXT_COLOR if zakljucane_celije[i][j] else TEXT_COLOR
                text = font.render(str(board[i][j]), True, text_color)
                screen.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 15))




#Marked cell
def oznacena_celija(cell):
    if cell is not None:
        vrsta, kolona = cell
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, (kolona * CELL_SIZE, vrsta * CELL_SIZE, CELL_SIZE, CELL_SIZE))




#Draw button
def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = button_font.render(text, True, text_color)
    screen.blit(button_text, (x + 10, y + 10))



#Check user solution
def check_solution(board, zakljucane_celije):
    for vrsta in range(9):
        for kolona in range(9):
            if not zakljucane_celije[vrsta][kolona]:
                broj = board[vrsta][kolona]
                board[vrsta][kolona] = 0
                if not validan_potez(board, vrsta, kolona, broj):
                    board[vrsta][kolona] = broj
                    return False
                board[vrsta][kolona] = broj
    return True



#Main function
def main():
    def reset_board():
        nonlocal board, zakljucane_celije, selektovana_celija, message
        board = generisi_sudoku()
        zakljucane_celije = [[board[i][j] != 0 for j in range(9)] for i in range(9)]
        selektovana_celija = None
        message = ""  #Clear the message

    
    board = generisi_sudoku()
    zakljucane_celije = [[board[i][j] != 0 for j in range(9)] for i in range(9)]
    selektovana_celija = None
    igra = True
    message = ""

    
    while igra:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                igra = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                x, y = event.pos
                if y > GRID_SIZE:

                    
                    if 20 <= x <= 140 and GRID_SIZE + 10 <= y <= GRID_SIZE + 50:
                        provera_resenja_sudoku(board)
                        zakljucane_celije = [[True] * 9 for _ in range(9)]  
                    elif 160 <= x <= 280 and GRID_SIZE + 10 <= y <= GRID_SIZE + 50:
                        reset_board()
                    elif 300 <= x <= 420 and GRID_SIZE + 10 <= y <= GRID_SIZE + 50:
                        if check_solution(board, zakljucane_celije):
                            message = "Tacno!"
                        else:
                            message = "Nije tacno(Nub si)."
                else:
                    selektovana_celija = (y // CELL_SIZE, x // CELL_SIZE)

            elif event.type == pygame.KEYDOWN:
                
                if selektovana_celija is not None:
                    vrsta, kolona = selektovana_celija
                    
                    if not zakljucane_celije[vrsta][kolona]:
                        if event.key == pygame.K_1:
                            board[vrsta][kolona] = 1
                        elif event.key == pygame.K_2:
                            board[vrsta][kolona] = 2
                        elif event.key == pygame.K_3:
                            board[vrsta][kolona] = 3
                        elif event.key == pygame.K_4:
                            board[vrsta][kolona] = 4
                        elif event.key == pygame.K_5:
                            board[vrsta][kolona] = 5
                        elif event.key == pygame.K_6:
                            board[vrsta][kolona] = 6
                        elif event.key == pygame.K_7:
                            board[vrsta][kolona] = 7
                        elif event.key == pygame.K_8:
                            board[vrsta][kolona] = 8
                        elif event.key == pygame.K_9:
                            board[vrsta][kolona] = 9
                        elif event.key == pygame.K_0 or event.key == pygame.K_BACKSPACE:
                            board[vrsta][kolona] = 0

        
        screen.fill(BACKGROUND_COLOR)
        oznacena_celija(selektovana_celija)
        ispis_brojeva(board, zakljucane_celije)
        
        nacrtaj_grid()

        draw_button("Solution", 20, GRID_SIZE + 10, 120, 40, BUTTON_COLOR, BUTTON_TEXT_COLOR)
        draw_button("Restart", 160, GRID_SIZE + 10, 120, 40, BUTTON_COLOR, BUTTON_TEXT_COLOR)
        draw_button("Done", 300, GRID_SIZE + 10, 120, 40, BUTTON_COLOR, BUTTON_TEXT_COLOR)
        
        if message:
            message_text = message_font.render(message, True, TEXT_COLOR)
            text_rect = message_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
            screen.blit(message_text, text_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()