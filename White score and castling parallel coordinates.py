# How castling affects the white scores in Sicilian games.
# Making the parallel coordinates chart.

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import matplotlib
from matplotlib import ticker
import numpy as np
import seaborn as sns
labels=["1000-1100","1100-1200","1200-1300","1300-1400","1400-1500","1500-1600","1600-1700",\
        "1700-1800","1800-1900","1900-2000","2000-2100","2100-2200","2300-2400",\
            "2700-2800"]
data = pd.read_csv('Scores.csv', encoding="utf-8")
pd.plotting.parallel_coordinates(data,"X",alpha=0.9,marker="o")
plt.legend(labels,bbox_to_anchor=(1.2, 1), loc=2, borderaxespad=0.)
plt.title("How castling affects the white scores in Sicilian games")
plt.show()
