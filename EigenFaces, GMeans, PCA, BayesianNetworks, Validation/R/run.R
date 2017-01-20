
#Q1
library(ISLR)

part1()
LOG_REG_WITH_VAL()
part3()

#Q2
library(pixmap)
# Path to the directory containing the images
input = '../data/faces-corrected'
PCA(input)

#Q3 - Gmeans
library(MASS);
library(nortest);
library(cluster);
library(ellipse);
# Path to the csv file
input = '../data/hw45-r3b-test-data.csv'
X = read.csv(input)
Gmeans(X, alpha=0.0001, k = 1)

#Q4
library(bnlearn)
input = '../data/bn-data.csv'
bayesian(input)