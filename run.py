import pygame
from PIL import ImageColor

pygame.init()

black = ImageColor.getrgb("black")
white = ImageColor.getrgb("white")
blue = ImageColor.getrgb("blue")
red = ImageColor.getrgb("red")
yellow = ImageColor.getrgb("yellow")

width = 200
height = 200

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TicTacToe")

clock = pygame.time.Clock()

top_row = [1, 2, 3]
central_row = [4, 5, 6]
bottom_row = [7, 8, 9]
left_column = [top_row[0], central_row[0], bottom_row[0]]
center_column = [top_row[1], central_row[1], bottom_row[1]]
right_column = [top_row[2], central_row[2], bottom_row[2]]
board_index = [top_row, central_row, bottom_row]

message = lambda text, color, position, size : screen.blit(pygame.font.SysFont("arial.ttf", size).render(
                                                     text, True, color), position
                                                    )

def check_win(board):
    board_values = []
    for i in range(3):
        board_values.append([x[0] for x in list(board.values()) if i * 3 < x[1] <= (i + 1) * 3])
    l = 0
    c = 0
    d1 = 0
    d2 = 0

    for i in range(len(board_values)):
        l = 0
        for j in range(len(board_values[i]) - 1):
            if board_values[i][j] == board_values[i][j + 1] and board_values[i][j] != 0:
                l += 1
                if l == 2:
                    return True
    for i in range(len(board_values[i])):
        c = 0
        for j in range(len(board_values) - 1):
            if board_values[j][i] == board_values[j + 1][i] and board_values[j][i] != 0:
                c += 1
                if c == 2:
                    return True

    for i in range(len(board_values) - 1):
        if board_values[i][i] == board_values[i + 1][i + 1] and board_values[i][i] != 0:
            d1 += 1
            if d1 == 2:
                return True
        if board_values[i][len(board_values) - 1 - i] == board_values[i + 1][len(board_values) - 2 - i] and board_values[i][j] != 0:
                d2 += 1
                if d2 == 2:
                    return True
    return False

def check_tie(board):
    z = 0
    for li in list(board.values()):
        if li[0] == 0:
            z += 1
    if z > 0:
        return False
    return True


def start():
    game_over = False
    close = False
    board = {(40, 40): [0, 1],
             (100, 40): [0, 2],
             (160, 40): [0, 3],
             (40, 100): [0, 4],
             (100, 100): [0, 5],
             (160, 100): [0, 6],
             (40, 160): [0, 7],
             (100, 160): [0, 8],
             (160, 160): [0, 9]}
    win = check_win(board)
    tie = (not check_win(board)) and check_tie(board)
    winner = 0

    player = 1
    t = []

    x1 = width / 2
    y1 = height / 2

    x1_add = 0
    y1_add = 0

    # cursor sides
    x2 = x1 + 7
    y2 = y1 + 7

    x3 = x2 + 3
    y3 = y2 - 4

    # posições centrais dos quadrados:
    # centro = (100, 100)
    # centro-cima = (100, 40)
    # centro-baixo = (100, 160)
    # centro-direita = (160, 100)
    # centro-esquerda = (40, 100)
    # topo-esquerda = (40, 40)
    # topo-direita = (160, 40)
    # fundo-esquerda = (40, 160)
    # fundo-direita = (160, 160)


    # cursor:
    # pygame.draw.polygon(screen, "red", [(x1, y1), (x2, y2), (x3, y3)])

    # table:
    # pygame.draw.line(screen, "white", [70, 10], [70, 190], width = 2)
    # pygame.draw.line(screen, "white", [130, 10], [130, 190], width = 2)
    # pygame.draw.line(screen, "white", [10, 70], [190, 70], width = 2)
    # pygame.draw.line(screen, "white", [10, 130], [190, 130], width = 2)

    # X:
    # pygame.draw.line(screen, "black", [300, 200], [310, 210], width=3)
    # pygame.draw.line(screen, "black", [300, 210], [310, 200], width=3)

    while not game_over:
        x1_add = 0
        y1_add = 0

        if any([win, tie]):
            close = True

        while close:
            if any([win, tie]):
                win, tie = False, False
            screen.fill("black")
            if winner != 0:
                message(f"Player {winner} wins", white, [10, 10], 25)
            else:
                message("TIE!", white, [10, 10], 25)
            message(f"Press Q to quit or G to play again", white, [10, 40], 15)
            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.type == pygame.QUIT:
                        game_over = True
                        close = False
                    if e.key == pygame.K_q:
                        game_over = True
                        close = False
                    if e.key == pygame.K_g:
                        start()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_over = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    x1_add = 0
                    y1_add = -60
                    if board[(x1, y1)][1] in top_row:
                        y1_add = 0
                elif e.key == pygame.K_DOWN:
                    x1_add = 0
                    y1_add = 60
                    if board[(x1, y1)][1] in bottom_row:
                        y1_add = 0
                elif e.key == pygame.K_RIGHT:
                    x1_add = 60
                    y1_add = 0
                    if board[(x1, y1)][1] in right_column:
                        x1_add = 0
                elif e.key == pygame.K_LEFT:
                    x1_add = -60
                    y1_add = 0
                    if board[(x1, y1)][1] in left_column:
                        x1_add = 0
                elif e.key == pygame.K_RETURN:
                    if board[(x1, y1)][0] == 0:
                        drawing_coord = (x1, y1)
                        x, y = drawing_coord
                        t.append([drawing_coord, player])
                        if player == 1:
                            board[(x1, y1)][0] = 1
                            player = 2
                            win = check_win(board)
                            tie = (not check_win(board)) and check_tie(board)
                            pygame.draw.line(screen, blue, [x - 10, y - 10], [x + 10, y + 10], width=3)
                            pygame.draw.line(screen, blue, [x - 10, y + 10], [x + 10, y - 10], width=3)
                            if win:
                                winner = 1
                            elif tie:
                                winner = 0
                        elif player == 2:
                            board[(x1, y1)][0] = 2
                            player = 1
                            win = check_win(board)
                            tie = (not check_win(board)) and check_tie(board)
                            pygame.draw.circle(screen, red, [x, y], 10)
                            if win:
                                winner = 2
                            elif tie:
                                winner = 0

        x1 += x1_add
        y1 += y1_add

        x2 = x1 + 7
        y2 = y1 + 7

        x3 = x2 + 3
        y3 = y2 - 4

        screen.fill(black)
        message(f"Player {player}'s turn", yellow, [0, 0], 18)
        pygame.draw.line(screen, "white", [70, 10], [70, 190], width = 2)
        pygame.draw.line(screen, "white", [130, 10], [130, 190], width = 2)
        pygame.draw.line(screen, "white", [10, 70], [190, 70], width = 2)
        pygame.draw.line(screen, "white", [10, 130], [190, 130], width = 2)
        for drawing in t:
            if drawing[1] == 1:
                x, y = drawing[0]
                pygame.draw.line(screen, blue, [x - 10, y - 10], [x + 10, y + 10], width=3)
                pygame.draw.line(screen, blue, [x - 10, y + 10], [x + 10, y - 10], width=3)
            if drawing[1] == 2:
                x, y = drawing[0]
                pygame.draw.circle(screen, red, [x, y], 14, width=2)

        pygame.draw.polygon(screen, yellow, [(x1, y1), (x2, y2), (x3, y3)])

        pygame.display.update()

        clock.tick(15)

    pygame.quit()
    quit()

start()
