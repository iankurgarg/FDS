CoinFlip <- function(){
	numberOfFlips=10000;
	a = matrix(nrow=numberOfFlips);
	b = matrix(nrow=numberOfFlips);
	sum = 0;
	for (i in 1:numberOfFlips) {
		coin = sample(0:1, 1);
		sum = sum + coin;
		a[i] = sum/i;
		b[i] = 0.5;
	}
	
	xrange=1:numberOfFlips;
	plot(xrange, a, type="l", xlab="Number of Coin Flips", ylab="Average", col="red", main="Average Coin Flip Value against the number of Coin Flips");

	lines(b, type="l", col="green");
}

CLT <- function(distribution, sampleSize, numSamples){
	result = matrix(nrow=numSamples);
	a = 0;
	if (distribution == "normal") {
		a = rnorm(10000);
	}
	else if(distribution == "uniform") {
		a = runif(10000);
	}
	else {
		return("Invalid distribution Name");
	}
	
	if(sampleSize > 35 || sampleSize < 29) {
		return("Invalid Sample Size");
	}
	
	if (numSamples < 100) {
		return("Invalid number of Samples");
	}
	
	for (i in 1:numSamples) {
		s = sample(a, size=sampleSize);
		result[i] = mean(s);
	}
	meanSamples = mean(result);
	sd = sd(result);
	var = var(result);
	d = density(result);
	plot(d, xlab="Mean of Samples", ylab="Density", main=paste(c("Sampling Distribution for mean", ""), collapse=""), col="red", type="l");
	
	cat(sprintf("Mean of the sampling dsitribution = %f\n", meanSamples));
	cat(sprintf("Variance of the sampling dsitribution = %f\n", var));
	cat(sprintf("Sigma*Sigma/n = %f\n", var(a)/sampleSize));
}

SLR <- function(input) {
	sales = read.csv(input);
	cols = colnames(sales);
	
	sales.TV.lm = lm(Sales ~ TV, data=sales);
	sales.Radio.lm = lm(Sales ~ Radio, data=sales);
	sales.Newspaper.lm = lm(Sales ~ Newspaper, data=sales);
	sales.TV.range=range(sales["TV"]);
	sales.Radio.range=range(sales["Radio"]);
	sales.Newspaper.range=range(sales["Newspaper"]);
	
	newdata.TV=data.frame(TV=sales.TV.range[1]:sales.TV.range[2])
	newdata.Radio=data.frame(Radio=sales.Radio.range[1]:sales.Radio.range[2])
	newdata.Newspaper=data.frame(Newspaper=sales.Newspaper.range[1]:sales.Newspaper.range[2])
	
	predictions.TV = predict(sales.TV.lm, newdata.TV);
	predictions.Radio = predict(sales.Radio.lm, newdata.Radio);
	predictions.Newspaper = predict(sales.Newspaper.lm, newdata.Newspaper);
	
	plot(Sales ~ TV, data=sales, main="Scatter plot for TV vs Sales", xlab="TV", ylab="Sales");
	lines(sales.TV.range[1]:sales.TV.range[2], predictions.TV, col="red");
	dev.new();
	plot(Sales ~ Radio, data=sales, main="Scatter plot for Radio vs Sales", xlab="Radio", ylab="Sales");
	lines(sales.Radio.range[1]:sales.Radio.range[2], predictions.Radio, col="red");
	dev.new();
	plot(Sales ~ Newspaper, data=sales, main="Scatter plot for Newspaper vs Sales", xlab="Newspaper", ylab="Sales");
	lines(sales.Newspaper.range[1]:sales.Newspaper.range[2], predictions.Newspaper, col="red");
}

MLR <- function(input) {
	sales = read.csv(input);
	
	sales.lm = lm(Sales ~ TV + Radio + Newspaper, data=sales);
	print (summary(sales.lm));
}

LogisticRegression <- function (input) {
	data = read.delim (input);
	data$Y = factor(data$Y);
	
	logit = glm(Y ~ X1 + X2 + X3, data = data, family="binomial");
	
	print(summary(logit))
}

LogisticRegressionImproved <- function (input) {
	data = read.delim (input);
	data$Y = factor(data$Y);
	
	logit = glm(Y ~ X1 + X2 + X3, data = data, family="binomial");
	print("---------------Before removal of outliers--------------------")
	print(summary(logit));
	
	e = studres(logit);
	em = matrix(e);
	outliers = which(abs(em)>3);
	datawithoutoutliers = which(abs(em) <= 2);
	
	newdata=data[datawithoutoutliers,];
	
	logit2 = glm(Y ~ X1 + X2 + X3, data=newdata, family="binomial", control=list(maxit=40));
	print('---------------After removal of outliers--------------------')
	print(summary(logit2));
	print(predict(logit2, type='response'))
}