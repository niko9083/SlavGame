# Vigtige ting til pygame
import pygame
from pygame.locals import *

# declare our global variables for the game
XO = "X"  # track whose turn it is; X goes first
grid = [[None, None, None], \
        [None, None, None], \
        [None, None, None]]

winner = None


def initBoard(ttt):
    # initialize the board and return it as a variable
    # ---------------------------------------------------------------
    # ttt : a properly initialized pyGame display variable

    # set up the background surface
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill(( 220, 220, 220))

    # linjerne
    # lodret lines...
    pygame.draw.line(background, (255, 0, 0), (215, 0), (215, 675), 10)
    pygame.draw.line(background, (0, 255, 0), (430, 0), (430, 675), 10)

    # vandret lines...
    pygame.draw.line(background, (255, 0, 0), (0, 245), (645, 245), 10)
    pygame.draw.line(background, (0, 255, 0), (0, 460), (645, 460), 10)
    pygame.draw.line(background, (0, 0, 255), (0,25), (645,25), 4)

    # return the board
    return (background)


def drawStatus(board):
    # draw the status (i.e., player turn, etc) at the bottom of the board
    # ---------------------------------------------------------------
    # board : the initialized game board surface where the status will
    #         be drawn

    # gain access to global variables
    global XO, winner

    # determine the status message
    if (winner is None):
        message = XO + "'s tur"
    else:
        message = winner + " VANDT!"

    # render the status message
    font = pygame.font.Font(None, 25)
    text = font.render(message, 1, (10, 10, 0))

    # copy the rendered message onto the board
    board.fill((128, 128, 128), (0, 0, 645, 24))
    board.blit(text, (300, 5))


def showBoard(ttt, board):
    # redraw the game board on the display
    # ---------------------------------------------------------------
    # ttt   : the initialized pyGame display
    # board : the game board surface

    drawStatus(board)
    ttt.blit(board, (0, 0))
    pygame.display.flip()


def boardPos(mouseX, mouseY):
    # given a set of coordinates from the mouse, determine which board space
    # (row, column) the user clicked in.
    # ---------------------------------------------------------------
    # mouseX : the X coordinate the user clicked
    # mouseY : the Y coordinate the user clicked

    # determine the row the user clicked
    if (mouseY < 244):
        row = 0
    elif (mouseY < 458):
        row = 1
    else:
        row = 2

    # determine the column the user clicked
    if (mouseX < 215):
        col = 0
    elif (mouseX < 430):
        col = 1
    else:
        col = 2

    # return the tuple containg the row & column
    return (row, col)


def drawMove(board, boardRow, boardCol, Piece):
    # draw an X or O (Piece) on the board in boardRow, boardCol
    # ---------------------------------------------------------------
    # board     : the game board surface
    # boardRow,
    # boardCol  : the Row & Col in which to draw the piece (0 based)
    # Piece     : X or O

    # determine the center of the square
    centerX = ((boardCol) * 215) + 108
    centerY = ((boardRow) * 225) + 125

    # draw the appropriate piece
    if (Piece == 'O'):
        pygame.draw.circle(board, (0, 0, 255), (centerX, centerY), 80, 7)
    else:
        pygame.draw.line(board, (0, 0, 255), (centerX - 66, centerY - 66), \
                         (centerX + 66, centerY + 66), 10)
        pygame.draw.line(board, (0, 0, 255), (centerX + 66, centerY - 66), \
                         (centerX - 66, centerY + 66), 10)

    # mark the space as used
    grid[boardRow][boardCol] = Piece


def clickBoard(board):
    # determine where the user clicked and if the space is not already
    # occupied, draw the appropriate piece there (X or O)
    # ---------------------------------------------------------------
    # board : the game board surface

    global grid, XO

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos(mouseX, mouseY)

    # make sure no one's used this space
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):
        # this space is in use
        return

    # draw an X or O
    drawMove(board, row, col, XO)

    # toggle XO to the other player's move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"


def gameWon(board):
    # determine if anyone has won the game
    # ---------------------------------------------------------------
    # board : the game board surface

    global grid, winner

    # check for winning rows
    # fixed
    for row in range(0, 3):
        if ((grid[row][0] == grid[row][1] == grid[row][2]) and \
                (grid[row][0] is not None)):
            # this row won
            winner = grid[row][0]
            pygame.draw.line(board, (255, 255, 255), (107, (row + 1) * 225 - 100), \
                             (540, (row + 1) * 225 - 100), 5)
            break

    # check for winning columns
    # fixed
    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
                (grid[0][col] is not None):
            # this column won
            winner = grid[0][col]
            pygame.draw.line(board, (255, 255, 0), ((col + 1) * 215 - 107, 125), \
                             ((col + 1) * 215 - 107, 575), 5)
            break

    # check for diagonal winners
    # fixing
    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
            (grid[0][0] is not None):
        # game won diagonally left to right
        winner = grid[0][0]
        pygame.draw.line(board, (0, 0, 255), (75, 100), (600, 600), 5)

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
            (grid[0][2] is not None):
        # game won diagonally right to left
        winner = grid[0][2]
        pygame.draw.line(board, (0, 0, 0), (250, 50), (50, 250), 5)


# --------------------------------------------------------------------
# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode((645, 675))
pygame.display.set_caption('Tic-Tac-Toe')

# create the game board
board = initBoard(ttt)

# main event loop
running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            clickBoard(board)

        # check for a winner
        gameWon(board)

        # update the display
        showBoard(ttt, board)