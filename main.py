import pygame as pg
import sys

def checkWin(mas, s):
    zeroes = 0

    for row in mas:
        zeroes += row.count(0)
        if row.count(s)==3:
            return s

    for col in range(3):
        if mas[0][col]==s and mas[1][col]==s and mas[2][col]==s:
            return s

    for col in range(3):
        if mas[0][0] == s and mas[1][1] == s and mas[2][2] == s:
            return s

    for col in range(3):
        if mas[0][2] == s and mas[1][1] == s and mas[2][0] == s:
            return s

    if zeroes == 0:
        return "Lol"

    return False


pg.init()

SIZE_SEGMEN = 100
MARGIN = 15

W = H = SIZE_SEGMEN*3 + MARGIN*4

sc = pg.display.set_mode((W, H))
pg.display.set_caption("TicTacToe")

BLACK = (0, 0, 0)
RED = (255,0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

mas = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

playerId = 'x'

gameOver = False

gameRun = True
while gameRun:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameRun = False
            pg.quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN and not gameOver:
            xM, yM = pg.mouse.get_pos()
            col = xM // (SIZE_SEGMEN + MARGIN)
            row = yM // (SIZE_SEGMEN + MARGIN)
            if mas[row][col] == 0:
                if playerId == 'x':
                    mas[row][col] = 'x'
                    playerId = 'o'
                elif playerId == 'o':
                    mas[row][col] = 'o'
                    playerId = 'x'
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            playerId = 'x'
            gameOver = False
            mas = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
            sc.fill(BLACK)

    if not gameOver:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    COLOR = GREEN
                elif mas[row][col] == 'o':
                    COLOR = RED
                else:
                    COLOR = WHITE

                x = col * SIZE_SEGMEN + (col + 1) * MARGIN
                y = row * SIZE_SEGMEN + (row + 1) * MARGIN
                pg.draw.rect(sc, COLOR, (x, y, SIZE_SEGMEN, SIZE_SEGMEN))
                if COLOR == GREEN:
                    pg.draw.line(sc, BLACK, (x+10, y+10), (x + SIZE_SEGMEN-10, y + SIZE_SEGMEN-10), 3)
                    pg.draw.line(sc, BLACK, (x + SIZE_SEGMEN-10, y+10), (x+10, y + SIZE_SEGMEN-10), 3)
                elif COLOR == RED:
                    pg.draw.circle(sc, BLACK, (x+SIZE_SEGMEN//2, y+SIZE_SEGMEN//2),SIZE_SEGMEN//2-5, 3)

    if playerId == 'x':
        gameOver = checkWin(mas, 'x')
    else:
        gameOver = checkWin(mas, 'o')

    if gameOver:
        sc.fill(BLACK)
        font = pg.font.SysFont('stxingkai', 80)
        text1 = font.render(gameOver, True, WHITE)
        text_rect = text1.get_rect()
        xT = sc.get_width() / 2 - text_rect.width / 2
        yT = sc.get_height() / 2 - text_rect.height / 2
        sc.blit(text1, [xT, yT])

    pg.display.update()


