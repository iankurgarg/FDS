library(bnlearn, quietly=TRUE);

bayesian <- function (input) {
	data = read.csv(input);
	data = data[, !(colnames(data) %in% c("X"))];
	res = hc(data);

	return(res$nodes[1]);
	plot(res);
	
	fit = bn.fit(res, data=data);
	return(fit);
}