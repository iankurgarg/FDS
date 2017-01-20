from Q_1 import part1
from Q_1 import LOG_REG_WITH_VAL
from Q_1 import part3
from Q_2 import PCA
from Q_3 import Gmeans
from Q_4 import bayesian
import pandas;

#Q1
# Path to Default.csv file from ISLR package
input = '../data/Default.csv'
part1(input)
LOG_REG_WITH_VAL(input)
LOG_REG_WITH_VAL(input)
LOG_REG_WITH_VAL(input)
part3(input)


#Q2
input = '../data/faces-corrected'
p = PCA(input);


#Q3
input = '../data/hw45-r3b-test-data.csv'
X = pandas.read_csv(input);
Gmeans(X, alpha=0.0001, k=1);

#Q4
# The output plot is saved as Q4.png in the current directory
input = '../data/bn-data.csv'
bayesian(input)
