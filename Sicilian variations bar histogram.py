# The histogram of the percentages of Sicilian variations
import chess.pgn
import numpy as np
import matplotlib.pyplot as plt
data = open('chessdata.pgn', encoding="utf-8")
N = 795173
def find_Index(array,string):
    index = 0
    for i in range(len(array)):
        if array[i] == string:
            index = i
    return index 

Sicilian_Openings_List = ['Paulsen/Kan','Taimanov','Kalashnikov/Loewenthal','Pelikan/Lasker/Sveshnikov',\
                     'Classical','Dragon','Accelerated Dragon','Najdorf','Scheveningen',\
                         'Rossolimo','Moscow/Sokolsky','Grand Prix/McDonell Attack','Closed Sicilian','Alapin',\
                     'Smith-Morra Gambit','Wing Gambit','Sicilian Sidelines']  
Sicilian_Openings = np.array(Sicilian_Openings_List)  
S = len(Sicilian_Openings)
occ_Sicilian = [0] *  S
index = -1
N_Total_Sicilian = 0
#for i in range(N):
 #   game = chess.pgn.read_game(data)
  #  Moves = str(game.mainline_moves())
   # opening = game.headers["Opening"]
    #if Moves[0:8] == '1. e4 c5': # i.e., if the opening is Sicilian
     #    N_Total_Sicilian = N_Total_Sicilian + 1
      #   if opening.find('Paulsen') != -1 or opening.find('Kan')!= -1 :
       #       index = find_Index(Sicilian_Openings,'Paulsen/Kan')             
        # elif:opening.find('Taimanov') != -1:
          #    index = find_Index(Sicilian_Openings,'Taimanov')
         #else:
             #   if opening.find('Kalashnikov') != -1 or opening.find('Loewenthal') != -1 :
              #       index = find_Index(Sicilian_Openings,'Kalashnikov/Loewenthal')
              #  else:
               #       if opening.find('Pelikan') != -1 or opening.find('Lasker') != -1 or opening.find('Sveshnikov') != -1 :
                #          index = find_Index(Sicilian_Openings,'Pelikan/Lasker/Sveshnikov')
                 #     else:
                  #        if opening.find('Classical') != -1 :
                   #           index = find_Index(Sicilian_Openings,'Classical')
                    #      else:
                     #         if opening.find('Dragon') != -1 and opening.find('Accelerated') == -1 :
                      #            index = find_Index(Sicilian_Openings,'Dragon')
                       #       else:
                        #          if opening.find('Accelerated Dragon') != -1:
                         #             index = find_Index(Sicilian_Openings,'Accelerated Dragon')
                          #        else:
                           #           if opening.find('Najdorf') != -1:
                            #              index = find_Index(Sicilian_Openings,'Najdorf')
                             #         else:
                              #            if opening.find('Scheveningen') != -1:
                               #                 index = find_Index(Sicilian_Openings,'Rossolimo')
                                  #            else:
                                   #               if opening.find('Sokolsky')!= -1:
                                     #                 index = find_Index(Sicilian_Openings,'Moscow/Sokolsky')
                                      #            else:
                                       #               if opening.find('Grand Prix') != -1 \
                                        #                  or opening.find('McDonell Attack') != -1:
                                         #                     index = find_Index(Sicilian_Openings,'Grand Prix/McDonell Attack')
                                          #            else:
                                           #               if opening.find('Closed') != -1:
                                            #                  index = find_Index(Sicilian_Openings,'Closed Sicilian')
                                             #             else:
                                              #                if opening.find('Alapin') != -1:
                                               #                   index = find_Index(Sicilian_Openings,'Alapin')
                                                #              else:
                                                    #              if opening.find('Smith-Morra Gambit') != -1:
                                                     #                     index = find_Index(Sicilian_Openings,'Smith-Morra Gambit')
                                                      #            else:
                                                       #               if opening.find('Wing Gambit')!= -1:
                                                        #                      index = find_Index(Sicilian_Openings,'Wing Gambit')
                                                         #             else:    
                                                          #                    index = find_Index(Sicilian_Openings,'Sicilian Sidelines')
 #   if index != -1:
  #      occ_Sicilian[index] = occ_Sicilian[index] + 1  
   #     index = -1 
occ_Sicilian = [2929,68,1437,932,708,1063,1287,1678,453,1650,177,485,4090,3708,3973,665,43715]  
for i in range(S):
    N_Total_Sicilian = N_Total_Sicilian + occ_Sicilian[i]

Per_Sicilian = [0] * S    
for j in range(S):    
    Per_Sicilian[j] = round((100 * occ_Sicilian[j] / float(N_Total_Sicilian)) ,2  )  

# by enhanced I mean after removing the last entity corresponding to the sidelines        
occ_Sicilian_enhanced = [2929,68,1437,932,708,1063,1287,1678,453,1650,177,485,4090,3708,3973,665]
Y = [4.24,0.1,2.08,1.35, 1.03, 1.54, 1.86, 2.43, 0.66, 2.39, 0.26, 0.7, 5.93, 5.37, 5.76, 0.96]
X = ['Paulsen/Kan','Taimanov','Kalashnikov/Loewenthal','Pelikan/Lasker/Sveshnikov',\
                     'Classical','Dragon','Accelerated Dragon','Najdorf','Scheveningen',\
                         'Rossolimo','Moscow/Sokolsky','Grand Prix/McDonell Attack','Closed Sicilian','Alapin',\
                     'Smith-Morra Gambit','Wing Gambit']
                          
# Y is the percentages of the Sicilian variation played
plt.style.use('classic')
plt.bar(X, height=Y,color='black')
plt.xticks(X)
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='heavy',
    fontsize='x-small'
)
plt.grid(axis='y',color='grey')
plt.xlabel('Sicilian Opening Variation')
plt.ylabel('Percentage of Sicilian Variation Played')
plt.title('Sicilian Variations Played in March 2013')
plt.show()
                










    
                          
                          
                          
