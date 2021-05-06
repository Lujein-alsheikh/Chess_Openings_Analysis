# Preparing the try3.csv file for the chart: The first 150 Sicilian games.
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import chess.pgn
import matplotlib
import numpy as np
data = open('chessdata.pgn', encoding="utf-8")
Sicilian_Openings_List = ['Paulsen/Kan','Taimanov','Kalashnikov/Loewenthal','Pelikan/Lasker/Sveshnikov',\
                     'Classical','Dragon','Accelerated Dragon','Najdorf','Scheveningen',\
                         'Rossolimo','Moscow/Sokolsky','Grand Prix/McDonell Attack','Closed Sicilian','Alapin',\
                     'Smith-Morra Gambit','Wing Gambit','Sicilian Sidelines'] 
def DidWhiteCastle ( Moves):
    res = "No"
    if Moves.find(". O-O ") != -1 or Moves.find(". O - O") != -1 :
        res =  "O-O"
    elif Moves.find(". O-O-O") != -1 or Moves.find(". O - O - O") != -1 :
        res = "O-O-O"
    return res 
Rating_diff = []
Sicilian_Variation = []
Result = []
Castling = []   
N = 3000
index = -1 
X = " "
Result2 = []
Variation2 = []
y = 0 
for i in range(N):
  game = chess.pgn.read_game(data)
  Moves = str(game.mainline_moves())
  opening = game.headers["Opening"]
  if Moves[0:8] == '1. e4 c5': # i.e., if the opening is Sicilian
      if game.headers["BlackElo"].find("?") == -1 and game.headers["WhiteElo"].find("?") == -1 :
          if 400 > int(game.headers["WhiteElo"]) - int(game.headers["BlackElo"]) > -400:
            index = index + 1
            if index < 150:  
               Rating_diff.append ((int(game.headers["WhiteElo"]) - int(game.headers["BlackElo"]))/40.0)   
               Result.append(game.headers["Result"])
               if game.headers["Result"] == "1-0":
                  Result2.append(8)
               elif game.headers["Result"] == "0-1":
                  Result2.append(-8)
               else : 
                  Result2.append(0)
               Castling.append(DidWhiteCastle(Moves))
               if opening.find('Paulsen') != -1 or opening.find('Kan')!= -1 :
                 X = 'Paulsen/Kan'    
                 y = -8
               elif opening.find('Taimanov') != -1:
                  X = 'Taimanov'
                  y = -7
               elif  opening.find('Kalashnikov') != -1 or opening.find('Loewenthal') != -1 :
                 X = 'Kalashnikov/Loewenthal'
                 y = -6
               elif opening.find('Pelikan') != -1 or opening.find('Lasker') != -1 or opening.find('Sveshnikov') != -1 :
                     X = 'Pelikan/Lasker/Sveshnikov'
                     y = -5
               elif opening.find('Classical') != -1 :
                     X = 'Classical'
                     y = -4
               elif opening.find('Dragon') != -1 and opening.find('Accelerated') == -1 :
                     X = 'Dragon'
                     y = -3
               elif opening.find('Accelerated Dragon') != -1:
                     X = 'Accelerated Dragon'
                     y = -2
               elif opening.find('Najdorf') != -1:
                   X = 'Najdorf'
                   y = -1 
               elif opening.find('Scheveningen') != -1:
                    X = 'Scheveningen'
                    y = 0 
               elif opening.find('Rossolimo')  != -1:
                   X = 'Rossolimo'
                   y = 1
               elif opening.find('Sokolsky')!= -1:
                    X = 'Moscow/Sokolsky'
                    y = 2
               elif opening.find('Grand Prix') != -1  or opening.find('McDonell Attack') != -1:
                   X = 'Grand Prix/McDonell Attack'
                   y = 3
               elif opening.find('Closed') != -1:
                   X = 'Closed Sicilian'
                   y = 4
               elif opening.find('Alapin') != -1:
                  X = 'Alapin'
                  y = 5
               elif opening.find('Smith-Morra Gambit') != -1:
                  X = 'Smith-Morra Gambit'
                  y = 6
               elif opening.find('Wing Gambit')!= -1:
                   X  = 'Wing Gambit'
                   y = 7
               else :  
                    X  = 'Sicilian Sidelines' 
                    y = 8
               Sicilian_Variation.append(X)      
               Variation2.append(y)
            else:
               break        
# after executing this code, I copied the results into a csv file named "try3.csv" in order to use this file to make the parallel coordinates chart:

data = pd.read_csv('trying3.csv', encoding="utf-8")
ax = plt.subplot()
ax2 = ax.twinx()
plt.yticks([-8,0,8],labels=["loss","draw","win"],) 
pd.plotting.parallel_coordinates(data,"White Castling",alpha = 0.9,marker="o")
plt.title("The first 150 Sicilian Games", fontweight='heavy')
mystr = """Var -8:Kan,-7:Taimanov, -6:Kalashnikov, -5:Pelikan,
 -4:Classical, -3:Dragon, -2:Accelerated Dragon, -1:Najdorf,
 0:Scheveningen, 1:Rossolimo, 2:Moscow, 3:Grand Prix, 4:Closed, 
5:Alapin, 6:Smith-Morra, 7:Wing Gambit, 8:Sidelines"""

ax.set_xlabel(mystr)
ax.set_ylim(-10,10)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
