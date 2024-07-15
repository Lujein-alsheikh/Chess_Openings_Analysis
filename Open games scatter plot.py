# The scattering plot for open games
import chess.pgn
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
data = open('chessdata.pgn', encoding="utf-8")
#List_All_Openings = ['Kings gambit','Bishops opening','Vienna opening','Poziani',\
 #                     'Center gambit','Russian game','Philidor defense',\
  #                        'Spanish opening','Three Knights opening','Italian opening',\
   #                    'Scotch opening','Alekhine defense','French defense','Caro-Kann defense',\
    #                   'Pirc/modern defense','Scandinavian defense','Sicilian defense',\
     #                   'The Dutch defense','Old Benoni','Trompowsky attack',\
      #                  'Benoni defense','Nimzo-Indian defense','Bogo-Indian defense',\
       #               'Queens Indian defense','Gruenfeld defense','Kings Indian defense',\
        #              'Veresov','Pseudo-Trompowsky','London system','Queens gambit',\
         #             'English opening','Reti opening','Kings Indian attack',\
          #            'Birds opening','Hungarian opening','Nimzo-Larsen attack']    
# All_Openings = np.array(List_All_Openings)  
Open_Openings = ["King's gambit",'Bishops opening','Vienna opening','Poziani',\
                          'Center gambit','Petroff defense','Philidor defense',\
                          'Spanish opening','Three Knights opening','Italian opening',\
                          'Scotch opening','Open Sidelines']
Colors = []
Rating1 = []
Rating2 = []       
N = 795173  
for i in range(N):
    game = chess.pgn.read_game(data)
    Moves = str(game.mainline_moves())
    if game.headers["WhiteElo"].find('?') == -1 and game.headers["BlackElo"].find('?') == -1:
     if Moves[0:8] == '1. e4 e5':
          Rating1.append(int(game.headers["WhiteElo"]))
          Rating2.append(int(game.headers["BlackElo"]))
          if Moves[12:14] == 'f4': # Kings gambit
              Colors.append(1) 
          elif Moves[12:15] == 'Bc4': # Bishops opening
              Colors.append(2)
          elif Moves[12:15] == 'Nc3': # Vienna opening
              Colors.append(3) 
          elif  Moves[12:19] == 'Nf3 Nf6': # Petroff defense
              Colors.append(4)
          elif  Moves[12:18] == 'Nf3 d6': # Philidor defense
              Colors.append(5)
          elif  Moves[12:26] == 'Nf3 Nc6 3. Bb5': # Spanish opening
              Colors.append(6)
          elif Moves[12:26] == 'Nf3 Nc6 3. Nc3': # Three Knights opening
              Colors.append(7)
          elif Moves[12:26] == 'Nf3 Nc6 3. Bc4': # Italian opening
              Colors.append(8)
          elif Moves[12:25] == 'Nf3 Nc6 3. d4': # Scotch opening
              Colors.append(9)   
          else: # Open Sidelines
              Colors.append(10)
              
cmap = matplotlib.colors.ListedColormap([ 'grey' ,'yellow', 'green', 'navy', 'hotpink', \
                                   'purple','aqua', 'black', 'red','lime' ])
bounds = np.linspace(0, 10, 11)
norm = matplotlib.colors.BoundaryNorm(bounds,cmap.N)
plt.xlabel('Rating of the first player (white)',fontweight='heavy')
plt.ylabel('Rating of the second player (black)',fontweight='heavy')
plt.xlim(700,2700)
plt.ylim(700,2700)
plt.title("Open Games' Types Played in March 2013", fontweight='heavy')
plt.scatter(Rating1 , Rating2 , c= Colors , s = 10, alpha=0.8,cmap=cmap,norm=norm)
labels = np.array([ 'Scotch opening', "King's Gambit" , "Bishop's opening",\
                 'Vienna opening'  ,\
                    'Petroff defense' , 'Philidor defense', 'Spanish opening',\
                     'Three Knights opening'  ,'Italian opening', 'Sidelines'])
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: labels[norm(x)])
plt.colorbar(ticks=np.arange(0.5,10,1),alpha=1,format = fmt)              
                        
#  if Moves[6:9] == 'Nf6':
            #    index = find_Index(Selected_Openings,'Alekhine defense')
             #else:
              # if Moves[6:8] == 'e6':
               #   index = find_Index(Selected_Openings,'French defense')     
               # else:
                 #  if Moves[6:8] == 'c6':
                  #     index = find_Index(Selected_Openings,'Caro-Kann defense')
                    #else:
                     #  if (Moves[6:8] == 'd6') | (Moves[6:8] == 'g6'):
                      #     index = find_Index(Selected_Openings,'Pirc/modern defense')
                       #else:
                        #   if Moves[6:8] == 'd5':
                         #      index = find_Index(Selected_Openings,'Scandinavian defense')
                         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
                
                
                
                
                
                
