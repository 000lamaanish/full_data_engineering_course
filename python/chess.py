
import pygame
import chess
import sys

# -------------------- Configuration --------------------

pygame.init()

WIDTH = 640
HEIGHT = 640
SQUARE_SIZE = WIDTH // 8

WHITE_SQUARE = (240, 217, 181)
BLACK_SQUARE = (181, 136, 99)
SELECTED_COLOR = (100, 200, 100)
MOVE_COLOR = (80, 160, 220)
BACKGROUND = (35, 35, 35)
TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT + 80))
pygame.display.set_caption("Python Chess Game")

font = pygame.font.SysFont("arial", 38, bold=True)
small_font = pygame.font.SysFont("arial", 22)

# -------------------- Chess Setup --------------------

board = chess.Board()

selected_square = None
legal_moves = []
game_message = "White's turn"

# White pieces use uppercase letters.
# Black pieces use lowercase letters.

PIECE_SYMBOLS = {
    "K": "K", "Q": "Q", "R": "R",
    "B": "B", "N": "N", "P": "P",
    "k": "k", "q": "q", "r": "r",
    "b": "b", "n": "n", "p": "p"
}


def get_piece_text(piece):
    """Return a readable symbol for a chess piece."""
    return PIECE_SYMBOLS[piece.symbol()]


def draw_board():
    """Draw the chessboard and its pieces."""

    for row in range(8):
        for col in range(8):

            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE

            # Alternate square colors.
            if (row + col) % 2 == 0:
                color = WHITE_SQUARE
            else:
                color = BLACK_SQUARE

            # Highlight the selected square.
            square = chess.square(col, 7 - row)

            if square == selected_square:
                color = SELECTED_COLOR

            pygame.draw.rect(
                screen,
                color,
                (x, y, SQUARE_SIZE, SQUARE_SIZE)
            )

            # Draw possible destinations.
            for move in legal_moves:
                if move.to_square == square:
                    center_x = x + SQUARE_SIZE // 2
                    center_y = y + SQUARE_SIZE // 2

                    pygame.draw.circle(
                        screen,
                        MOVE_COLOR,
                        (center_x, center_y),
                        10
                    )

            # Draw the piece.
            piece = board.piece_at(square)

            if piece:
                symbol = get_piece_text(piece)

                piece_color = (
                    (255, 255, 255)
                    if piece.color == chess.WHITE
                    else (25, 25, 25)
                )

                text = font.render(
                    symbol,
                    True,
                    piece_color
                )

                # Outline makes white pieces easier to see.
                outline_color = (
                    (20, 20, 20)
                    if piece.color == chess.WHITE
                    else (230, 230, 230)
                )

                outline = font.render(
                    symbol,
                    True,
                    outline_color
                )

                rect = text.get_rect(
                    center=(
                        x + SQUARE_SIZE // 2,
                        y + SQUARE_SIZE // 2
                    )
                )

                outline_rect = rect.copy()

                screen.blit(
                    outline,
                    outline_rect.move(2, 2)
                )

                screen.blit(text, rect)


