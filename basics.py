import chess.pgn
import matplotlib
from matplotlib import pyplot as plt

data = open('Data/lichess_db_standard_rated_2014-03.pgn', encoding="utf-8")
# the number of games
N = 795173 

# First, count for each Event type.
List = []
N_Classic =0
N_Blitz =0
N_Bullet = 0
N_Other =0
for i in range(N):
    game = chess.pgn.read_game(data)
    if game.headers["Event"] == 'Rated Classical game':
        N_Classic = N_Classic + 1
    else:
        if game.headers["Event"] == 'Rated Blitz game':
            N_Blitz = N_Blitz + 1
        else:
            if game.headers["Event"] == 'Rated Bullet game':
                 N_Bullet = N_Bullet + 1 
            else:
                N_Other = N_Other + 1
              
print(N_Classic, N_Blitz, N_Bullet, N_Other) 

'''
# N_Classic = 269294
# N_Blitz = 285058
# N_Bullet = 220030
# N_Other = 20791
Classic_Per = N_Classic/float(N)
Blitz_Per = N_Blitz/float(N)
Bullet_Per = N_Bullet/float(N)
print(Classic_Per, Blitz_Per, Bullet_Per)
'''

'''
# Second, see all openings played:
Openings = []
game = chess.pgn.read_game(data)
previous = game.headers["Opening"]
Openings.append(previous)
for i in range(N):
    game = chess.pgn.read_game(data)
    if game.headers["Opening"] not in Openings:
        Openings.append(game.headers["Opening"])
    
M = len(Openings)   
print(Openings) 

Classical = [0] * M
Blitz = [0] * M
Bullet = [0] * M

# Third, for each opening, I compute how many classic, blitz, or bullet were played
# Group by opening and then by event type
for i in range(N):
    game = chess.pgn.read_game(data)
    for j in range(M): 
        if Openings[j] == game.headers["Opening"]:
            if game.headers["Event"] == 'Rated Classical game':
                Classical[j] = Classical[j] + 1
            else:
                if game.headers["Event"] == 'Rated Blitz game':
                      Blitz[j] = Blitz[j] + 1
                else:
                    if game.headers["Event"] == 'Rated Bullet game':
                         Bullet[j] = Bullet[j] + 1

                         
# Fourth, I calculate the percentages    
occ = [0] * M
for i in range(M):
    occ[i] = Classical[i] + Bullet[i] + Blitz[i]
Classical_Per = [0] * M
for i in range(M):
    Classical_Per[i] = Classical[i] * 100/float(occ[i])
      
# Fifth, check if there are other reasons to finish a game other than normal of time forfeit.    
Terminations = ['Normal','Time forfeit']
for i in range(N):
    game = chess.pgn.read_game(data)
    if (game.headers["Termination"] != 'Normal') and (game.headers["Termination"] != 'Time forfeit'):
        Terminations.append(game.headers["Termination"])


# Sixth, I was trying to find out the ratios of games with increment  
Classic_With_Increment = ['600+10']
N_With = 0
Classic_With_Out_Increment = ['900+0']
N_WithOut = 0
Blitz_Time_Control = ['240+0']
for i in range(N):
     game = chess.pgn.read_game(data)
     if game.headers["Event"] == 'Rated Classical game':
                 if game.headers["TimeControl"][4] != 0:
                     N_With = N_With + 1
                 else:
                     N_WithOut = N_WithOut + 1
'''


    

    
