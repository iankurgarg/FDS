from rpy2.robjects import r;

def bayesian (input):
    r('library(bnlearn, quietly=TRUE)');
    r('input = "'+input+'"');
    r('data = read.csv(input)');
    r('data = data[, !(colnames(data) %in% c("X"))]');
    r('res = hc(data)');
    r('png("Q4.png")')
    r('plot(res)');
    r('dev.off()');
    r('fit = bn.fit(res, data=data)');
    r('print(fit)');

