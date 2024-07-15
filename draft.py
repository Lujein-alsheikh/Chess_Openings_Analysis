import chess.pgn
"""
# Creating a sample game:

data = open('Data/lichess_db_standard_rated_2014-03.pgn', encoding="utf-8")
game = chess.pgn.read_game(data)
# <class 'chess.pgn.Game'>
print(type(game))
print(game)

if game is not None:
        # Save the game to a new PGN file
        with open('sample_game.pgn', 'w', encoding='utf-8') as output:
            exporter = chess.pgn.FileExporter(output)
            game.accept(exporter)
""" 

""" 
# Trying out the pgn2data library

from converter.pgn_data import PGNData

pgn_data = PGNData("Data/sample_game.pgn")
result = pgn_data.export()
result.print_summary()
"""
data = open('Data/lichess_db_standard_rated_2014-03.pgn', encoding="utf-8")
game = chess.pgn.read_game(data)
# <class 'chess.pgn.Game'>
print(type(game))
print(game)
print("----------------------------------------------------------------")
print(game.mainline_moves())