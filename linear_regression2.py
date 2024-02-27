# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:09:37 2024

@author: renuk
"""

#Multiple correlation regression analysis
import pandas as pd
import numpy as np
import seaborn as sns
cars=pd.read_csv('cars.csv')
#Exploratory data analysis

cars.describe()
#Graphical represenation
import matplotlib.pyplot as plt
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.displot(cars.HP)
#data is right skewed
plt.boxplot(cars.HP)
#There are several outliers in HP columns
#Similar operations are expected for other three column
sns.displot(cars.MPG)
#data is slightly left distributed
plt.boxplot(cars.MPG)
#There are no outliers
sns.displot(cars.VOL)
#data is slightly left distributed
plt.boxplot(cars.VOL)
sns.displot(cars.SP)
#data is slightly right distributed
plt.boxplot(cars.SP)
#There are several outliers
sns.displot(cars.WT)
plt.boxplot(cars.WT)
#There are several outliers
#Now let us plot joint plot
#histogram
import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars['MPG'])

#Now let us plot count plot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
#Count plot shows how many times the each value occur
#92 HP value occur 7 times

#QQ plot 
from scipy import stats
import pylab
stats.probplot(cars.MPG,dist="norm",plot=pylab)
plt.show()
#MPG data is normally distributed
#There are 10 scatter plots need to be plotted,one by one
#to plot,so we can use pair plots




import seaborn as sns
sns.pairplot(cars.iloc[:,:])
#linearity: direction : and Strength :
#You can check the collinearity problem between the input
# you can check plot between sp and hp 
#same way you can check wt and vol

cars.corr()
#you can check sp and hp, r value os 0.97 



import statsmodels.formula.api as smf
ml1=smf.ols('MPG-WT+VOL+SP+HP',data=cars).fit()
ml1.summary()
#r square valuse obsersed s 0.771c0.85
#p values of wt and vol is 0.814, and 0.556


import statsmodels.api as sm
sm.graphics.influence_plot(ml1)


cars_new=cars.drop(cars.index[[76]])
##again apply regression to car_new
ml_new=smf.ols('MPG-WT+VOL+SP+HP',data=cars_new).fit()
ml_new.summary()

rsq_hp=smf.ols('HP-WT+VOL+SP',data=cars).fit().rsquared
vif_hp=1/(1-rsq_hp)
vif_hp


rsq_wt=smf.ols('WT-HP+VOL+SP',data=cars).fit().rsquared
vif_wt=1/(1-rsq_wt)
vif_wt

rsq_vol=smf.ols('VOL-HP+WT+SP',data=cars).fit().rsquared
vif_vol=1/(1-rsq_vol)
vif_vol

rsq_sp=smf.ols('SP-HP+WT+VOL',data=cars).fit().rsquared
vif_sp=1/(1-rsq_sp)
vif_sp

d1={'Variables':['HP','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
vif_frame=pd.DataFrame(d1)
vif_frame

final_ml=smf.ols('MPG-VOL+SP+HP',data=cars_new).fit()
final_ml.summary()

####prediction 

pred=final_ml.predict(cars)

##QQ plot

res=final_ml.resid
sm.qqplot(res)
plt.show()

stats.probplot(res,dist='norm',plot=pylab)
plt.show()


sns.residplot(x=pred,y=cars.MPG,lowess=True)
plt.xlabel('Fitted')
plt.ylabel('Residual')
