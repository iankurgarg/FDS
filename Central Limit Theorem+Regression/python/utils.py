import numpy as np;
import matplotlib.pyplot as plt;
from scipy import stats;
import pandas as pd;
from sklearn import linear_model as lm;
import warnings;

def CoinFlip ():
    numberOfFlips = 10000;
    a = [None]*numberOfFlips;
    b = [None]*numberOfFlips;
    sum = 0;
    for i in range(0,numberOfFlips):
        coin = np.random.choice(2, 1);
        sum = sum + coin;
        a[i] = sum / i;
        b[i] = 0.5;

    xrange = list(range(0,numberOfFlips));
    plt.plot(xrange, a);
    plt.plot(xrange, b);
    plt.xlabel("Number of Coin Flips");
    plt.ylabel("Average");
    plt.title("Average Coin Flip Value vs the number of Coin Flips");
    plt.show();

def CLT (distribution, sampleSize, numSamples):

    result = [None]*numSamples;
    a = 0;
    if (distribution == "normal"):
        a = stats.norm.rvs(size=10000);
    elif (distribution == "uniform"):
        a = stats.uniform.rvs(size=10000);

    for i in range(0,numSamples):
        s = np.random.choice(a, size=sampleSize);
        result[i] = np.mean(s);

    meanSamples = np.mean(result);
    sd = np.std(result);
    var = np.var(result);

    d = stats.gaussian_kde(result);
    xs = np.linspace(min(result), max(result), 200);
    d.covariance_factor = (lambda : 0.5);
    d._compute_covariance();
    plt.plot(xs, d(xs));
    plt.show();
    #plot(d, xlab="Mean of Samples", ylab="Density", main=paste(c("Sampling Distribution for mean", ""), collapse=""), col="red", type="l");

    print("Mean of the sampling dsitribution = ", meanSamples);
    print("Variance of the sampling dsitribution = ", var);
    print("Sigma*Sigma/n = ", np.var(a) / sampleSize);


def SLR (input):
    sales = pd.read_csv(input);
    print(len(sales.TV.values));
    regr_model = lm.LinearRegression();
    salesTVlm = regr_model.fit(sales.TV.to_frame(), sales.Sales.to_frame());
    plt.scatter(sales.TV.to_frame(), sales.Sales.to_frame(), linestyle="-", color='black', linewidths=1);
    plt.plot(sales.TV.to_frame(), regr_model.predict(sales.TV.to_frame()), color='blue', linewidth=1);
    plt.xlabel("TV");
    plt.ylabel("Sales");
    plt.title("Sales vs TV");
    plt.show();

    salesRadiolm = regr_model.fit(sales.Radio.to_frame(), sales.Sales.to_frame());
    plt.scatter(sales.Radio.to_frame(), sales.Sales.to_frame(), linestyle="-", color='black', linewidths=1);
    plt.plot(sales.Radio.to_frame(), regr_model.predict(sales.Radio.to_frame()), color='blue', linewidth=1);
    plt.xlabel("Radio");
    plt.ylabel("Sales");
    plt.title("Sales vs Radio");
    plt.show();

    salesNewspaperlm = regr_model.fit(sales.Newspaper.to_frame(), sales.Sales.to_frame());
    plt.scatter(sales.Newspaper.to_frame(), sales.Sales.to_frame(), linestyle="-", color='black', linewidths=1);
    plt.plot(sales.Newspaper.to_frame(), regr_model.predict(sales.Newspaper.to_frame()), color='blue', linewidth=1);
    plt.xlabel("Newspaper");
    plt.ylabel("Sales");
    plt.title("Sales vs Newspaper");
    plt.show();

def MLR (input):
    warnings.filterwarnings(action="ignore", module="scipy");
    sales = pd.read_csv(input);
    regr_model = lm.LinearRegression();
    independentX = sales.TV.to_frame();
    independentX['Radio'] = sales.Radio;
    independentX['Newspaper'] = sales.Newspaper;
    regr_model.fit(independentX, sales.Sales.to_frame());
    print("Coefficients:\n", regr_model.coef_);
    print("Intercept:\n", regr_model.intercept_);

def LogisticRegression (input):
    return;

def LogisticRegressionImproved (input):
    return;