# bar histogram for games' types
import chess.pgn
import matplotlib
from matplotlib import pyplot as plt
data = open('chessdata.pgn', encoding="utf-8")
N = 795173 # the total number of games
N_Classic =0
N_Blitz =0
N_Bullet = 0
N_Blitz_tour = 0
N_Classical_tour = 0
N_Bullet_tour = 0
N_Correspondence= 0
#for i in range(N):
 #   game = chess.pgn.read_game(data)
   #  if game.headers["Event"] == 'Rated Classical game':
      #  N_Classic = N_Classic + 1
   # else:
    #    if game.headers["Event"] == 'Rated Blitz game':
      #      N_Blitz = N_Blitz + 1
       # else:
        #    if game.headers["Event"] == 'Rated Bullet game':
         #        N_Bullet = N_Bullet + 1 
          #  else:
           #      if game.headers["Event"] == 'Rated Correspondence game':
         #                      N_Correspondence = N_Correspondence + 1
         #        else:
  #                   if game.headers["Event"][0:22] == 'Rated Blitz tournament':
   #                       N_Blitz_tour = N_Blitz_tour + 1
    #                 else:
     #                     if game.headers["Event"][0:23] == 'Rated Bullet tournament':
                #                 N_Bullet_tour = N_Bullet_tour + 1
          #               else: 
           #                    if game.headers["Event"][0:26] == 'Rated Classical tournament':
            #                            N_Classical_tour = N_Classical_tour + 1 
N_Correspondence = 2357
N_Classic = 269294
N_Blitz = 285058
N_Bullet = 220030               
N_Blitz_tour = 6716
N_Bullet_tour = 11285
N_Classical_tour = 594

# there are 161 more games than the given N. All these games are Classical
# tournament games.

N_tour = N_Blitz_tour + N_Bullet_tour + N_Classical_tour
N_normal = N_Classic + N_Blitz + N_Bullet

Per_Corr = N_Correspondence * 100 /float(N)
Per_tour = N_tour * 100 /float(N)   
Per_normal =   N_normal * 100 /float(N)
# print(N_Blitz_tour, N_Bullet_tour, N_Correspondence, N_tour, Per_Corr, Per_tour)

# the per of normal classic games:
Classic_Per = round((N_Classic * 100 /float(N)),2)
Blitz_Per =round(( N_Blitz * 100 /float(N)),2)
Bullet_Per = round((N_Bullet * 100/float(N)),2)   

N_total_classic = N_Classic + N_Classical_tour
N_total_Blitz = N_Blitz + N_Blitz_tour
N_total_Bullet = N_Bullet + N_Bullet_tour 
            
Classic_per_in_tour = N_Classical_tour * 100 /float(N_tour)    
Blitz_per_tour = N_Blitz_tour * 100/float(N_tour)
Bullet_per_tour = N_Bullet_tour * 100/float(N_tour)
    

Openings = [] 
game = chess.pgn.read_game(data)
x = game.headers["Opening"]
#Openings.append(x)

# N_Italian = 24663
# N_Spanish = 2020

#for i in range(N):
 #   game = chess.pgn.read_game(data)
  #  if game.headers["Opening"] not in Openings:
   #    Openings.append(game.headers["Opening"])
M = len(Openings) 
# M = 2530

Bullet_tour_per = 100*N_Bullet_tour/float(N)
Blitz_tour_per = 100*N_Blitz_tour/float(N)
Y1 = [ round(Bullet_Per,2), round(Blitz_Per,2),round(Classic_Per,2)]
Y2 = [round(Bullet_tour_per,2),round(Blitz_tour_per,2),round((100*N_Classical_tour/float(N)),2)]
Y3 = [round((100*N_total_Bullet/float(N)),2), round((100*N_total_Blitz/float(N)),2),round((100*N_total_classic/float(N)),2)]

X0=['Bullet','Blitz','Classic']         
plt.bar(X0, height=Y1,color='b', alpha = 0.6,label = 'normal games')
plt.bar(X0, height = Y2, color = 'red',alpha=0.5, label = 'tournament games')
#plt.bar(X0, height = Y3, color = 'black',alpha=0.5, label = 'all games')
plt.legend(loc='upper left')
plt.xticks(X0)
plt.xticks(
    #rotation=45, 
    horizontalalignment='right',
    fontweight='heavy',
    fontsize='x-small'
)
plt.grid(axis='y',color='grey')
plt.xlabel('Game type',fontweight='heavy')
plt.ylabel('Percentage',fontweight='heavy')
plt.title("Game types for March 2013",fontweight='heavy')
plt.show() 















    
    
    
    
