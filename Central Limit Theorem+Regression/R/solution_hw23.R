#cleanup before start
rm(list=ls(all=T))


####
# Path variables to files
#
####
setwd('.') #Inside code folder - DON'T CHANGE THIS PATH
#source('installPackages.R')
source('utils.R')
path_to_data_folder = '../data' # DON'T CHANGE THIS PATH 
library(MASS)
library(stats)

#Q1 
CoinFlip() 


#Q2
populationDistribution = 'normal'
sampleSize = 30
numberOfSamples = 120
CLT(populationDistribution,sampleSize,numberOfSamples)

#Q3a
SLR(paste(path_to_data_folder,'/hw23R-Advertising.csv',sep=''))

#Q3b 
MLR(paste(path_to_data_folder,'/hw23R-Advertising.csv',sep=''))

#Q4
LogisticRegression(paste(path_to_data_folder,'/hw23R-q4.txt',sep=''))

#Q5
LogisticRegressionImproved(paste(path_to_data_folder,'/hw23R-q4.txt',sep=''))

