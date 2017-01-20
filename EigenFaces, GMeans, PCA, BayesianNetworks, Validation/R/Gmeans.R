####################################################################
# Implement G-means algorithm                                      #
####################################################################

library(MASS);
library(nortest);
library(cluster);
library(ellipse);

#p = 2;
#X1 = matrix(runif(p*p), p, p);
#COV = crossprod(X1);
#mu = c(40,50);
#mu = c(0,0);
#n = 100;
#x1 = mvrnorm(n, mu, matrix(c(10,6,5,6), 2, 2));
#mu = c(10,20);
#x2 = mvrnorm(n, mu, matrix(c(3,1,1,6), 2, 2));
#mu = c(40,50);
#x3 = mvrnorm(n, mu, matrix(c(12,11,11,16), 2, 2));
#x = rbind(x1, x2, x3);




# X is the input dataset(it is a dataframe contain multiple cols reading from csv file)
Gmeans <- function(X,alpha = 0.0001,k=1){
#  set.seed(1);
	C1 = kmeans(X, k)$centers;
	C2 = rbind(C1, C1);
	
	while (dim(C1)[1] != dim(C2)[1]) {
		res = kmeans(X, C1);	
		C2 = res$centers;
		
		subX = X[res$cluster == 1,]
		C1 = SubGMeans(subX, alpha, C2[1, ]);
		
		i = 2;
		if (dim(C2)[1] > 1) {
			for (i in 2:dim(C2)[1]) {
				subX = X[res$cluster == i,]
				C3 = SubGMeans(subX, alpha, C2[i, ]);
				C1 = rbind(C1, C3);
			}
		}
	}
	
	res = kmeans(X, C1);
	
	if (dim(X)[2] == 2) {
  	#clusplot(x, res$cluster, lines=0, shade=TRUE, color=TRUE,main="Clusters", xlab="X", ylab="Y");
  	plot(x, col=res$cluster,main="Clusters", xlab="X", ylab="Y");
  	points(res$centers, pch=20, col="blue");
  	i = 1;
  	for (i in 1:(length(res$centers)/2)) {
  	  lines(ellipse(cov(X[res$cluster == i,]), centre = res$centers[i,], level=0.68), col="blue");
  	  lines(ellipse(cov(X[res$cluster == i,]), centre = res$centers[i,], level=0.95), col="blue");
  	  lines(ellipse(cov(X[res$cluster == i,]), centre = res$centers[i,], level=0.99), col="blue");
  	}
	}
	else if (dim(X)[2] > 2){
	  plot3d(res, X);
	}
	
return (res);
}

SubGMeans <- function (x, alpha, c) {
#  set.seed(4);
  c = kmeans(x, t(as.matrix(c)))$centers;
	C = kmeans(x, 2);
	cc = C$centers;
	
	c1 = cc[1,];
	c2 = cc[2,];
	
	v = c1-c2;
	
	modV = norm(v, type="2");
	
	projectedX = as.matrix(x) %*% as.matrix(v);
	projectedX = projectedX/modV;
	
	scaledX = scale(projectedX);
	
  if (dim(scaledX)[1] <= 7) {
    return(c);
  }
	res = ad.test(scaledX);
	
	p = res$p.value;
	
	if (p < alpha) {
		return(C$centers);
	}
	else {
		return(c);
	}
}

plot3d <- function (C, X) {
  cc = C$centers;
  d = dim(cc)[2];
  if (d >= 2) {
    
    ds = as.integer(sqrt(d));
    dss = 0;
    if (ds*ds == (d*(d-1)/2)) {
      #par(mfrow=c(ds,ds));
    }
    else if ((ds+1)*ds > (d*(d-1)/2)) {
      #par(mfrow=c(ds+1,ds));
    }
    else {
      #par(mfrow=c(ds+1,ds+1));
    }
    
    for (p in 1:d) {
      for (q in 1:d) {
        if (p < q){
          s = c(p,q);
          plot(X[,s], col=C$cluster,main="Clusters", xlab=paste("X", p, sep=""), ylab=paste("X", q, sep=""));
          points(cc[,s], pch=20, col="blue");

          i = 1;
          for (i in 1:(dim(C$centers)[1])) {
            lines(ellipse(cov(X[C$cluster == i,s]), centre = C$centers[i,s], level=0.68), col=i+1);
            lines(ellipse(cov(X[C$cluster == i,s]), centre = C$centers[i,s], level=0.95), col=i+1);
            lines(ellipse(cov(X[C$cluster == i,s]), centre = C$centers[i,s], level=0.99), col=i+1);
          }
          print(paste ("plotted", p, q, sep=""));
        }
      }
    }
  }
}

