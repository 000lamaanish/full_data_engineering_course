
# import pygame
# import chess
# import sys

# # -------------------- Configuration --------------------

# pygame.init()

# WIDTH = 640
# HEIGHT = 640
# SQUARE_SIZE = WIDTH // 8

# WHITE_SQUARE = (240, 217, 181)
# BLACK_SQUARE = (181, 136, 99)
# SELECTED_COLOR = (100, 200, 100)
# MOVE_COLOR = (80, 160, 220)
# BACKGROUND = (35, 35, 35)
# TEXT_COLOR = (255, 255, 255)

# screen = pygame.display.set_mode((WIDTH, HEIGHT + 80))
# pygame.display.set_caption("Python Chess Game")

# font = pygame.font.SysFont("arial", 38, bold=True)
# small_font = pygame.font.SysFont("arial", 22)

# # -------------------- Chess Setup --------------------

# board = chess.Board()

# selected_square = None
# legal_moves = []
# game_message = "White's turn"

# # White pieces use uppercase letters.
# # Black pieces use lowercase letters.

# PIECE_SYMBOLS = {
#     "K": "K", "Q": "Q", "R": "R",
#     "B": "B", "N": "N", "P": "P",
#     "k": "k", "q": "q", "r": "r",
#     "b": "b", "n": "n", "p": "p"
# }


# def get_piece_text(piece):
#     """Return a readable symbol for a chess piece."""
#     return PIECE_SYMBOLS[piece.symbol()]


# def draw_board():
#     """Draw the chessboard and its pieces."""

#     for row in range(8):
#         for col in range(8):

#             x = col * SQUARE_SIZE
#             y = row * SQUARE_SIZE

#             # Alternate square colors.
#             if (row + col) % 2 == 0:
#                 color = WHITE_SQUARE
#             else:
#                 color = BLACK_SQUARE

#             # Highlight the selected square.
#             square = chess.square(col, 7 - row)

#             if square == selected_square:
#                 color = SELECTED_COLOR

#             pygame.draw.rect(
#                 screen,
#                 color,
#                 (x, y, SQUARE_SIZE, SQUARE_SIZE)
#             )

#             # Draw possible destinations.
#             for move in legal_moves:
#                 if move.to_square == square:
#                     center_x = x + SQUARE_SIZE // 2
#                     center_y = y + SQUARE_SIZE // 2

#                     pygame.draw.circle(
#                         screen,
#                         MOVE_COLOR,
#                         (center_x, center_y),
#                         10
#                     )

#             # Draw the piece.
#             piece = board.piece_at(square)

#             if piece:
#                 symbol = get_piece_text(piece)

#                 piece_color = (
#                     (255, 255, 255)
#                     if piece.color == chess.WHITE
#                     else (25, 25, 25)
#                 )

#                 text = font.render(
#                     symbol,
#                     True,
#                     piece_color
#                 )

#                 # Outline makes white pieces easier to see.
#                 outline_color = (
#                     (20, 20, 20)
#                     if piece.color == chess.WHITE
#                     else (230, 230, 230)
#                 )

#                 outline = font.render(
#                     symbol,
#                     True,
#                     outline_color
#                 )

#                 rect = text.get_rect(
#                     center=(
#                         x + SQUARE_SIZE // 2,
#                         y + SQUARE_SIZE // 2
#                     )
#                 )

#                 outline_rect = rect.copy()

#                 screen.blit(
#                     outline,
#                     outline_rect.move(2, 2)
#                 )

#                 screen.blit(text, rect)


# def update_message():
#     """Update the game status."""

#     global game_message

#     if board.is_checkmate():
#         winner = "Black" if board.turn == chess.WHITE else "White"
#         game_message = f"Checkmate! {winner} wins!"

#     elif board.is_stalemate():
#         game_message = "Stalemate! Draw!"

#     elif board.is_insufficient_material():
#         game_message = "Draw: insufficient material!"

#     elif board.is_check():
#         player = "White" if board.turn == chess.WHITE else "Black"
#         game_message = f"{player} is in check!"

#     else:
#         player = "White" if board.turn == chess.WHITE else "Black"
#         game_message = f"{player}'s turn"


# def handle_click(position):
#     """Handle square selection and piece movement."""

#     global selected_square, legal_moves

#     mouse_x, mouse_y = position

#     # Ignore clicks outside the board.
#     if mouse_y >= HEIGHT:
#         return

#     col = mouse_x // SQUARE_SIZE
#     row = mouse_y // SQUARE_SIZE

#     clicked_square = chess.square(col, 7 - row)

#     # If a piece is already selected, attempt a move.
#     if selected_square is not None:

#         attempted_move = chess.Move(
#             selected_square,
#             clicked_square
#         )

#         piece = board.piece_at(selected_square)

#         # Automatically promote a pawn to a queen.
#         if (
#             piece
#             and piece.piece_type == chess.PAWN
#             and chess.square_rank(clicked_square)
#             in (0, 7)
#         ):
#             attempted_move = chess.Move(
#                 selected_square,
#                 clicked_square,
#                 promotion=chess.QUEEN
#             )

#         if attempted_move in legal_moves:
#             board.push(attempted_move)

#             selected_square = None
#             legal_moves = []

#             update_message()
#             return

#     # Select a piece belonging to the current player.
#     piece = board.piece_at(clicked_square)

#     if piece and piece.color == board.turn:
#         selected_square = clicked_square

#         legal_moves = [
#             move
#             for move in board.legal_moves
#             if move.from_square == selected_square
#         ]

#     else:
#         selected_square = None
#         legal_moves = []


# def draw_status():
#     """Display whose turn it is and the game status."""

#     pygame.draw.rect(
#         screen,
#         BACKGROUND,
#         (0, HEIGHT, WIDTH, 80)
#     )

#     status_text = small_font.render(
#         game_message,
#         True,
#         TEXT_COLOR
#     )

#     screen.blit(status_text, (15, HEIGHT + 10))

#     help_text = small_font.render(
#         "Click a piece, then its destination | R: Restart",
#         True,
#         (190, 190, 190)
#     )

#     screen.blit(help_text, (15, HEIGHT + 42))


# def restart_game():
#     """Reset the board to its starting position."""

#     global board, selected_square, legal_moves

#     board = chess.Board()
#     selected_square = None
#     legal_moves = []

#     update_message()


# # -------------------- Main Game Loop --------------------

# clock = pygame.time.Clock()
# running = True

# update_message()

# while running:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#         elif event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_ESCAPE:
#                 running = False

#             elif event.key == pygame.K_r:
#                 restart_game()

#             elif event.key == pygame.K_u:
#                 if board.move_stack:
#                     board.pop()
#                     selected_square = None
#                     legal_moves = []
#                     update_message()

#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 handle_click(event.pos)

#     screen.fill(BACKGROUND)

#     draw_board()
#     draw_status()

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.exit()
