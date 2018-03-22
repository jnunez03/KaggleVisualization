import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pandas import Series, DataFrame
from pylab import *
import statsmodels.api as sm
from pandas_datareader import data, wb
from toolz import partitionby
from matplotlib.ticker import MaxNLocator
from scipy import stats
import scipy as sp
import re
from scipy.stats import norm
import squarify # pip install !
from pylab import rcParams
from scipy.stats import spearmanr
from pandas.tools.plotting import scatter_matrix
from matplotlib import pyplot as plt, font_manager
plt.style.use('fivethirtyeight')
rcParams['figure.figsize'] = 12,9
#plt.style.use('ggplot')        
# Reading in the data
df = pd.read_csv("/Users/justinnunez/Downloads/20170817.csv")  

# Data types of our variables. Also checks if they are in proper format. 
df.info()        

# Check for Null Values
df.isnull().sum()     
# sz_top, sz_bot, exit_velocity, launch_angle, hit_direction have missing values.

    
df.tail(n=15)
df.columns
print(df.shape) 
df.info()
# .describe() function which prints summary statistics of only numerical data
# We can see that it only outputted data for year and hours which are int/float variables. 
# this just states that our numbers aren't being read as numbers but as objects, plain variables.
df.describe()


# Let's make a function to get us the pitch count. 
df["pitcher"].value_counts() # this gives up the pitch count for each pitcher in the game!
sb.despine() # plot function for aesthetics.
my_colors = ['navy','orangered','orangered','navy','orangered','orangered','navy','navy']
df["pitcher"].value_counts().plot(kind='bar', color=my_colors)
plt.yticks(weight='bold',color='black')
plt.xticks(fontsize=10,rotation=0, weight='bold',color='black')
plt.text(x=0, y = 115, s= 'Pitch Count for Each Pitcher',fontsize = 24, weight = 'bold', alpha = .75)    
plt.text(x=0, y = 111.8, s= 'Orange: Mets    Navy: Yankees',fontsize = 13, weight = 'bold', alpha = .65)        
    
# We can get total pitch count by team based on the catchers!
df["catcher"].value_counts().plot(kind='bar', colors=my_colors)
labels = ["Yankees","Mets"]
df["catcher"].value_counts().values # Shows me 153, 143
x0 = [0,1]
plt.xticks(x0,labels,fontsize=13,rotation=0, weight='bold',color='black')
plt.text(x=-.65, y = 170, s= 'Team Pitch Count',fontsize = 30, weight = 'bold', alpha = .75)    


# Which pitches were thrown and by starting pitcher!
# Met's Starter
x = df[df["pitcher"] == "Matz, Steven"]["pitch_type"].value_counts().values
y = df[df["pitcher"] == "Matz, Steven"]["pitch_type"].value_counts().index     
sb.barplot(x=x, y=y, palette='RdBu_d', saturation=1)
plt.yticks(weight='bold',color='black',fontsize=12)
plt.text(x=0, y =-.76, s= 'Steven Matz Pitches Count',fontsize = 27.5, weight = 'bold', alpha = .75)

# Yanks Starter
x1= df[df["pitcher"] == "Severino, Luis"]["pitch_type"].value_counts().values
y1 = df[df["pitcher"] == "Severino, Luis"]["pitch_type"].value_counts().index     
sb.barplot(x=x1, y=y1, palette='Blues_d', saturation=1)
plt.yticks(weight='bold',color='black',fontsize=12)
plt.text(x=0, y =-.76, s= 'Luis Severino Pitches Count',fontsize = 27.5, weight = 'bold', alpha = .75)

## Major differences in the types of pitches used. How about as a team!
df.groupby(["catcher"])["pitch_type"].value_counts().plot(kind='bar')

## FF = Four-Seam Fastball
## FS = Fastball (sinker, splitter)
## FC = Fastball (cutter)
## FT = Two-Seam
# Other way of plotting this...
# Which pitches were thrown and by which team
""" Take subset where catcher is gary and other is ..."""      
yankspitches = df[df["catcher"] == "Sanchez, Gary"]["pitch_type"].value_counts().index
metspitches = df[df["catcher"] == "d'Arnaud, Travis"]["pitch_type"].value_counts().index
yvals = df[df["catcher"] == "Sanchez, Gary"]["pitch_type"].value_counts().values
zvals = df[df["catcher"] == "d'Arnaud, Travis"]["pitch_type"].value_counts().values
fig = plt.figure(figsize=(12,9))
ax0 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
fig.suptitle("Pitch Usage by the... \n\n\n",fontweight='bold', fontsize=22)
ax0.title.set_text('Yankees')
ax2.title.set_text('Mets')
ax0.set_ylabel('Pitch Usage                         ', weight='bold',rotation=0, fontsize=15)
#ax2.set_ylabel('Pitch Usage',rotation=0)
#plt.tight_layout()
sb.barplot(x=yankspitches, y=yvals, palette='BuGn_d', saturation=1, ax=ax0)
sb.barplot(x=metspitches, y=zvals, palette='RdBu_d', saturation=1, ax=ax2)


# Pitch Speed!! 

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
# Pitch Speed!!
""" TAKE THESE PLOTS FROM COMPUTER AT WORK """ 
ticks_font = font_manager.FontProperties(family='Calibri')
fte_graph = df.groupby("pitcher")["rel_speed"].mean().plot(figsize=(9,6),marker='s',linewidth=2.4)
fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 18)
fte_graph.set_yticklabels(labels = [-10, '84   ', '86   ', '88   ', '90   ', '92   ','94   ','96 mph ',])
fte_graph.axhline(y = 83, color = 'black', linewidth = .9, alpha = .7)
fte_graph.set_xlim(left = 0, right = 8)
#fte_graph.xticks(range(0,8,1),fontsize=10,color='black')
fte_graph.xaxis.label.set_visible(False)
fte_graph.set_xticklabels(fte_graph.get_xticklabels(),fontsize = 9,rotation=40,ha="right",color='black')
fte_graph.text(x = -.6, y = 79.1,
   s = '_____________________________________________________________________________________',
   color = 'grey', alpha = .7)
fte_graph.text(x=-.6, y = 78.5, s='By: Justin Nunez                                                                                                                Source: New York Mets',
              fontsize=4, color='grey',fontproperties=ticks_font)
fte_graph.text(x=-.035, y=96.7, s='Yankees Throw Harder on Average',horizontalalignment='left',fontsize = 26, weight = 'bold', alpha = .75)


df["pitch_call"] = df["pitch_call"].astype(str)
df.event_type.value_counts()
df["pitch_call"].value_counts()
# What heights are called strikes and balls!

Ball = df[(df["pitch_call"] == "BallCalled")]
Strike = df[(df["pitch_call"] == "StrikeCalled" )]


## These plots from macbook tho
Ball.boxplot(column='plate_loc_z',by='pitch_call')
Strike.boxplot(column='plate_loc_z',by='pitch_call')

Ball.boxplot(column='rel_speed',by='pitch_call')
Strike.boxplot(column='rel_speed',by='pitch_call')


""" TAKE ABOVE PLOTS FROM COMPUTER AT WORK """ 



rcParams['figure.figsize'] = 12,8
df.boxplot(column='plate_loc_z',by='pitch_call')
df.boxplot(column='plate_loc_x',by='pitch_call')
plt.figure()

""" Batter's BOX """
### Batter's box, color coated
df_dummies = pd.get_dummies(df['pitch_call'])
df_dummies.head()

df_new = pd.concat([df, df_dummies], axis=1)
df_new.head()
df_new.columns
df_new[:6]
del df_new['pitch_call']

## FOR ALL BATTERS ! 


sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new, hue='StrikeCalled', fit_reg=False)
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new, hue='BallCalled', fit_reg=False)
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new, hue='FoulBall', fit_reg=False)
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new, hue='HitByPitch', fit_reg=False)
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new, hue='InPlay', fit_reg=False)
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new, hue='StrikeSwinging', fit_reg=False)
""" Just to check my dummy variables worked"""
newdf = df_new[df_new.columns[27:38]]
newdf.head()

## We can do the same for Met's batters and Yankees Batters...
yankspitches = df[df["catcher"] == "Sanchez, Gary"] # When Yanks  pitch - Mets bat
metspitches = df[df["catcher"] == "d'Arnaud, Travis"] # when mets pitch - Yanks bat
ax3 = plt.subplots()
                # METS BATTERS
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new[df_new["catcher"] == "Sanchez, Gary"], hue='StrikeCalled', fit_reg=False)
                # Yankees batters
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new[df_new["catcher"] == "d'Arnaud, Travis"], hue='StrikeCalled', fit_reg=False)
               # METS BATTING
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new[df_new["catcher"] == "Sanchez, Gary"], hue='BallCalled', fit_reg=False)
                # Yankees batters
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new[df_new["catcher"] == "d'Arnaud, Travis"], hue='BallCalled', fit_reg=False)
               # Mets batters
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new[df_new["catcher"] == "Sanchez, Gary"], hue='StrikeSwinging', fit_reg=False)
              # Yankees batters
sb.lmplot('plate_loc_x', 'plate_loc_z', data=df_new[df_new["catcher"] == "d'Arnaud, Travis"], hue='StrikeSwinging', fit_reg=False)

""" END OF PITCHES LOCATION PLOTS """ 

#     -    -    -    -    -    -  # 
""" NEW: Pitch Speed by batter """

df.groupby(['batter'])['rel_speed'].mean().sort_values().plot(kind='bar')
df.groupby(['batter'])['rel_speed'].max().sort_values().plot(kind='bar')

# Check pitching speed
sb.distplot(df["rel_speed"],kde=False)
sm.qqplot(df["rel_speed"], line='q')
sp.stats.mstats.normaltest(df["rel_speed"], axis=0) # shows data is normal! p-value < statistic value

                          
df.groupby(['pitch_call'])["rel_speed"].mean().plot()
df.groupby(['pitch_call'])["rel_speed"].median().plot()






df.groupby(['pitch_type'])["rel_speed"].mean().plot()
df.groupby(['pitch_type'])["rel_speed"].median().plot()




""" SPEED OR PITCH TYPE RELATED TO HIT OUTCOME? """

# We know something was hit when it has an exit velocity to it and ball is InPlay!  Let's take that subset!
pitchesHIT = df[(df['exit_velocity'] > 0) & (~df['launch_angle'].isnull()) & (~df['hit_direction'].isnull()) & (metspitches["pitch_call"] == "InPlay")]
# Check for any correlation
sb.heatmap(pitchesHIT.corr())

# _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _  _ _ _ _ _ _ __  _ _ _ _ _ __ _ _ _ _ _ __------------__#


""" 3-2 counts!     # # # # # # # # # # # # # # # # # # # # # # # # """

metspitches = df[df["catcher"] == "d'Arnaud, Travis"] # subset of mets pitches only. 

# how many 3-2 counts were there.
x = metspitches[(metspitches["balls"] == 3) & (metspitches["strikes"] == 2)]
len(x)

# This locates are 3-2 counts so we can see what happened after them
#  5, 27, 83, 141, 262, 272
metspitches.loc[(metspitches["balls"] == 3) & (metspitches["strikes"] == 2)] 
# obj.ix[val1, val2] - Select both rows and columns
metspitches.ix[[5,27,83,141,262,272], ["batter","event_type"]]

""" 3-2 counts finished """ 

# - _____________- --___________________________________________________________ --- - _ --

""" Dangerous Hitter """
yankspitches = df[df["catcher"] == "Sanchez, Gary"] # When Yanks  pitch - Mets bat
metspitches = df[df["catcher"] == "d'Arnaud, Travis"] # when mets pitch - Yanks bat

hits = ("single", "home_run", "double", "triple")
# One Method                
HitsAgainst = metspitches[(metspitches["event_type"] == "home_run") & (~metspitches["exit_velocity"].isnull()) & (metspitches["pitch_call"] == "InPlay")]  

HitsAgainst["batter"] # Gary Sanchez is the batter with the homerun!

""" END OF DANGEROUS HITTER """

""" START OF YANKS AND METS BATTING BAR GRAPH WHEN BALL IS IN PLAY """

metspitches.event_type.value_counts()

metspitches[metspitches["pitch_call"] == "InPlay"]["event_type"].value_counts() # what occured
# Lets plot it! 

### YANKEES BATTING PLOT ! 
b1=metspitches[metspitches["pitch_call"] == "InPlay"]["event_type"].value_counts().index
b2=metspitches[metspitches["pitch_call"] == "InPlay"]["event_type"].value_counts().values

#sb.barplot(x=b1, y=b2, palette='BuGn_d', saturation=1)
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax8.text(rect.get_x()+rect.get_width()/2., 1.0, '%d'%int(height),
                ha='center', va='bottom')

N = 6
ind = np.arange(N)
LEFT = -0.020

fig, ax8 = plt.subplots()
fig.suptitle('Breakdown of Yankees Batting',
             horizontalalignment='left',
             weight='bold', fontsize=24,
             x=LEFT, y=1.03)
fig.text(LEFT,.975, "When balls were considered In-Play.",
         horizontalalignment='left',
         weight='medium', fontsize=15, color='#555555')
rects1 = ax8.bar(ind,b2)
# add some text for labels, title and axes ticks
ax8.set_ylabel('Occurrences', rotation='horizontal', horizontalalignment='left')
ax8.yaxis.set_label_coords(LEFT, 1.03)
ax8.spines['top'].set_visible(False)
ax8.spines['right'].set_visible(False)
ax8.get_xaxis().tick_bottom()
ax8.get_yaxis().tick_left()
ax8.xaxis.grid(False)
ax8.set_xticks(ind)
ax8.set_xticklabels(('Field Out', 'Single', 'Home Run', 'Error', 'Double Play', 'Double'), weight='medium')
plt.setp(ax8.get_yticklabels(), fontproperties=ticks_font)
plt.setp(ax8.get_xticklabels(), fontproperties=ticks_font)
autolabel(rects1)

# PLOT METS BATTING
yankspitches[yankspitches["pitch_call"] == "InPlay"]["event_type"].value_counts() # what occured
d1=yankspitches[yankspitches["pitch_call"] == "InPlay"]["event_type"].value_counts().index
d2=yankspitches[yankspitches["pitch_call"] == "InPlay"]["event_type"].value_counts().values

               
fig1, ax9 = plt.subplots()
fig1.suptitle('Breakdown of Mets Batting',
             horizontalalignment='left',
             weight='bold', fontsize=24,
             x=LEFT, y=1.03)
fig1.text(LEFT,.975, "When balls were considered In-Play.",
         horizontalalignment='left',
         weight='medium', fontsize=15, color='#555555')
rects2 = ax9.bar(ind,d2)
# add some text for labels, title and axes ticks
ax9.set_ylabel('Occurrences', rotation='horizontal', horizontalalignment='left')
ax9.yaxis.set_label_coords(LEFT, 1.03)
ax9.spines['top'].set_visible(False)
ax9.spines['right'].set_visible(False)
ax9.get_xaxis().tick_bottom()
ax9.get_yaxis().tick_left()
ax9.xaxis.grid(False)
ax9.set_xticks(ind)
ax9.set_xticklabels(('Field Out', 'Single', 'Force Out', 'Double', 'Error', 'Home Run'), weight='medium')
plt.setp(ax9.get_yticklabels(), fontproperties=ticks_font)
plt.setp(ax9.get_xticklabels(), fontproperties=ticks_font)
autolabel(rects2)


"""  - -  END of PLOTTING METS AND YANKEES BATTING FOR BALLS IN PLAY - - """

# ^ ^ ^ ^ ^^ ^ ^ ^ ^ ^ ^  ^ ^ ^ ^ ^ ^  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ #





      
# Check numerical pitch variables and find a correlation!
newdf = df[df.columns[15:25]]
df.pitch_call.value_counts()
sb.pairplot(newdf)
rcParams['figure.figsize'] = 16,12
sb.heatmap(newdf.corr())
scatter_matrix(newdf, alpha=.6, figsize=(20,16), diagonal='kde')
#Scatter Matrix
