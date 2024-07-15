# Histogram of white score, ranges of 100 points
import chess.pgn
import numpy as np
import matplotlib.pyplot as plt
data = open('chessdata.pgn', encoding="utf-8")
N = 795173
# I will cover the range of ratigns from 1000 to 2500
white_win = [0]*15 
draw = [0]*15
Num_games = [0]*15
avg = 0
#for i in range(N):
 #   game = chess.pgn.read_game(data)
  #  Moves = str(game.mainline_moves())
   # if Moves[0:8] == '1. e4 c5': # i.e., if the opening is Sicilian
    #  white_rating = int(game.headers["WhiteElo"])
     # black_rating = int(game.headers["BlackElo"])
      #avg = round( ( (white_rating + black_rating)/2.0),2)
      #for j in range(15):
       #   if 1000 + j*100  <= avg < 1000 + (j+1)*100 :
        #      Num_games[j] = Num_games[j] + 1 
         #     if game.headers["Result"] == '1-0':
          #        white_win[j] = white_win[j] + 1 
           #   elif game.headers["Result"] == '1/2-1/2':
            #      draw[j] = draw[j] + 1

#print(Num_games,'\n',white_win,'\n',draw)
Num_games = [40, 286, 1221, 3969, 7813, 11870, 12655, 12674, 9687, 5333, 2332, 686, 161, 58, 50]
white_win = [23, 127, 529, 1882, 3627, 5593, 5927, 5927, 4657, 2580, 1031, 302, 67, 38, 34]
draw = [1,8,28,85,192,349,405,455,375,222,136,34,13,5,7]
black_win = [0]*15

for k in range(15):
    black_win[k] = Num_games[k] - white_win[k] - draw[k]

X = [' ']*15
for i in range(15):
    X[i] = str(1000+ i*100)+'-'+str(1000+(i+1)*100)
    
white_win_per = [0]*15
black_win_per = [0]*15
draw_per = [0]*15 

for i in range(15):
    white_win_per[i] = round((100* white_win[i]/ float(Num_games[i])),2)
    black_win_per[i] = round((100* black_win[i]/ float(Num_games[i])),2)
    draw_per[i] = round((100 * draw[i]/ float(Num_games[i])),2)
    
White_Scores = [0]*15
Black_Scores = [0]*15

for i in range(15):
   White_Scores[i] = round(( white_win_per[i] + (1/2) * draw_per[i] ) ,2)
   Black_Scores[i] =  round(( black_win_per[i] + (1/2) * draw_per[i]) ,2)

plt.bar(X, height=White_Scores,color='slateblue',label = 'White Scores = white wins % + 1/2 draws %')
plt.xticks(X)
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='heavy',
    fontsize='x-small'
)
plt.legend(loc='upper left')
plt.grid(axis='y',color='grey')
plt.xlabel("The average of the players' ratings ",fontweight='heavy')
plt.ylabel('White Scores',fontweight='heavy')
plt.title("How the scores against Sicilian opening change with the players' ratings",fontweight='heavy')
plt.show()    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
