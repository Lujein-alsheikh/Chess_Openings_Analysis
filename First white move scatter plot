# Scatter plot for first move
import numpy as np
import matplotlib.pyplot
from matplotlib import pyplot as plt
import chess.pgn
from pylab import *
data = open('chessdata.pgn', encoding="utf-8")
N = 795173
Rating1 = []
Rating2 = []
Open_Opening = ['Kings gambit','Bishops opening','Vienna opening','Poziani',\
                          'Center gambit','Russian game','Philidor defense',\
                          'Spanish opening','Three Knights opening','Italian opening',\
                          'Scotch opening','Open Sidelines']

Openings = [] 
First_Move = []
Two_letters_moves= ['e4','d4' , 'c4','g3', 'f4','b3']
for i in range(N):
    game = chess.pgn.read_game(data)
    Moves = str(game.mainline_moves())
    #Openings.append(game.headers["Opening"])
    if game.headers["WhiteElo"].find('?') == -1 and game.headers["BlackElo"].find('?') == -1:
     if Moves[3:5] in Two_letters_moves:
        First_Move.append(Moves[3:5])
        Rating1.append(int(game.headers["WhiteElo"]))
        Rating2.append(int(game.headers["BlackElo"]))
     elif Moves[3:6] == 'Nf3':
        First_Move.append(Moves[3:6])
        Rating1.append(int(game.headers["WhiteElo"]))
        Rating2.append(int(game.headers["BlackElo"]))
     else:
        First_Move.append('other')
        Rating1.append(int(game.headers["WhiteElo"]))
        Rating2.append(int(game.headers["BlackElo"]))
        
M = len(First_Move)                
colors2 = [' '] * M
for i in range(M):
   if First_Move[i] == 'e4':
       #colors2[i] = 'red'
       colors2[i] = 1
   elif First_Move[i] == 'd4':
       #colors2[i] = 'salmon'
       colors2[i] = 2
   elif First_Move[i] == 'c4':
       #colors2[i] = 'grey'
       colors2[i] = 3
   elif First_Move[i] == 'g3':
       #colors2[i] = 'black'
       colors2[i] = 4
   elif First_Move[i] == 'f4':
       #colors2[i] = 'firebrick'
       colors2[i] = 5
   elif First_Move[i] == 'b3':
       #colors2[i] = 'navy'
       colors2[i] = 6
   elif First_Move[i] == 'Nf3':
       #colors2[i] = 'deeppink'
       colors2[i] = 8
   elif First_Move[i] == 'other'  :
       #colors2[i] == 'violet'
       colors2[i] = 7
  
x = Rating1
y = Rating2
colors = colors2
cmap = matplotlib.colors.ListedColormap(['grey' ,'yellow', 'green', 'navy', 'crimson', 'rebeccapurple',\
                                         'black', 'red' ])
# define the bins and normalize
bounds = np.linspace(0, 8, 9)
norm = matplotlib.colors.BoundaryNorm(bounds,cmap.N)
plt.xlabel('Rating of the first player (white)',fontweight='heavy')
plt.ylabel('Rating of the second player (black)',fontweight='heavy')
plt.xlim(700,2700)
plt.ylim(700,2700)
plt.title("First Moves Chosen in the Games", fontweight='heavy')
plt.scatter(x, y, c= colors , s = 10, alpha=0.8,cmap=cmap,norm=norm)
labels = np.array(['other', 'e4','d4','c4','g3','f4','b3','Nf3'])
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: labels[norm(x)])
plt.colorbar(ticks=np.arange(0.5,8,1),alpha=1,format = fmt)










