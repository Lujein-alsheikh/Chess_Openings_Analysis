import zstandard
import shutil
from tqdm import tqdm


# this code is taken from the github account: 
# https://github.com/ManasiTilak/pgn_zst_unzipper/tree/main

def decompress_zstd(input_file, output_file):
    with open(input_file, 'rb') as compressed_file:
        decompressor = zstandard.ZstdDecompressor()
        with decompressor.stream_reader(compressed_file) as reader:
            with open(output_file, 'wb') as decompressed_file:
                decompressed_file.write(reader.read())

input_file = "/home/fhernandez/Documents/Github_repositories/Chess_Openings_Analysis/Data/lichess_db_standard_rated_2014-03.pgn.zst"
output_file = "/home/fhernandez/Documents/Github_repositories/Chess_Openings_Analysis/Data/lichess_db_standard_rated_2014-03.pgn"

decompress_zstd(input_file, output_file)
