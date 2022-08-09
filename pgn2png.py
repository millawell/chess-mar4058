import chess.pgn
import chess.svg
from cairosvg import svg2png
from PIL import Image
from io import BytesIO

colors = ["#ced27b", "#aaa346"]

with  open("mar4058_1.pgn", "r") as  fin:
    game = chess.pgn.read_game(fin)

board = game.end().board()

squares = [game.end().move.from_square, game.end().move.to_square]

svgw = chess.svg.board(
    board,
    fill={
        square: colors[(square % 2) == ((square//8) % 2)] 
        for square in squares
    }
)

svgb = chess.svg.board(
    board,
    fill={
        square: colors[(square % 2) == ((square//8) % 2)] 
        for square in squares
    },
    flipped=True
)

pngw = BytesIO()
pngb = BytesIO()
svg2png(
    bytestring=svgw.encode("utf-8"),
    write_to=pngw,
    parent_width=1024,
    parent_height=1024,
)

svg2png(
    bytestring=svgb.encode("utf-8"),
    write_to=pngb,
    parent_width=1024,
    parent_height=1024,
)

imgw = Image.open(pngw)
imgb = Image.open(pngb)

merged_image = Image.new('RGB',(imgw.size[0]+imgb.size[0], imgw.size[1]), (250,250,250))
merged_image.paste(imgw,(0,0))
merged_image.paste(imgb,(imgw.size[0],0))

merged_image.save("board_mar4058_1.png","PNG")