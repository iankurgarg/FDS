from utils import *;
####
# Path variables to files
#
####
path_to_data_folder = '../data' # DON'T CHANGE THIS PATH

#Q1
CoinFlip()


#Q2
# populationDistribution: string('uniform','normal')
# sampleSize: integer (~30)
# numberOfSamples: integer (>100)
populationDistribution = "normal";
sampleSize = 30;
numberOfSamples = 200;
CLT(populationDistribution,sampleSize,numberOfSamples)

#Q3a
SLR(path_to_data_folder+'/hw23R-Advertising.csv');

#Q3b
MLR(path_to_data_folder+'/hw23R-Advertising.csv')

#Q4
LogisticRegression(path_to_data_folder+'/hw23R-q4data.txt')

#Q5
LogisticRegressionImproved(path_to_data_folder+'/hw23R-q4data.txt')

