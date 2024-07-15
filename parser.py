# working with chess.pgn takes ages. I will parse the games to create a .csv and
# later work with pandas data frames.

# This code is from chatgpt and I still need to check it before using it!

import csv
import chess.pgn

# Function to parse a single game and return a list of the relevant information
def parse_game(game):
    return [
        game.headers.get("Event", ""),
        game.headers.get("Site", ""),
        game.headers.get("Round", ""),
        game.headers.get("White", ""),
        game.headers.get("Black", ""),
        game.headers.get("Result", ""),
        game.headers.get("UTCDate", ""),
        game.headers.get("WhiteElo", ""),
        game.headers.get("BlackElo", ""),
        game.headers.get("WhiteRatingDiff", ""),
        game.headers.get("BlackRatingDiff", ""),
        game.headers.get("ECO", ""),
        game.headers.get("Opening", ""),
        game.headers.get("TimeControl", ""),
        game.headers.get("Termination", ""),
        game.mainline_moves().variations[0] if game.variations else ""
    ]

# Open the PGN file
pgn_file = open("yourfile.pgn")

# Open a CSV file for writing
csv_file = open("games_data.csv", mode="w", newline='', encoding="utf-8")
csv_writer = csv.writer(csv_file)

# Write the header row
csv_writer.writerow(["Event", "Site", "Date", "Round", "White", "Black", "Result", "ECO", "WhiteElo", "BlackElo", "Moves"])

# Read and write each game
while True:
    game = chess.pgn.read_game(pgn_file)
    if game is None:
        break
    game_data = parse_game(game)
    csv_writer.writerow(game_data)

# Close the files
pgn_file.close()
csv_file.close()

print("Data has been successfully written to games_data.csv")
