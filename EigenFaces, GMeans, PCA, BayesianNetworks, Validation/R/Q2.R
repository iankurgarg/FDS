library(pixmap);

#input = 'Google Drive/Courses/Sem 1/CSC 591 - FDS/Homeworks/Homework 4-5/';

PCA <- function (input) {
	a = list.files(input, full.names=TRUE);
	data = array(NA, c(length(as.vector(getChannels(read.pnm(a[1])))), length(a)))
	for (i in 1:length(a)) {
		image = read.pnm(a[i]);
		k = as.vector(getChannels(image));
		data[,i] = k;
	}
	
	mean = rowMeans(data);
	
	avgImage = pixmapGrey(matrix(mean, nrow=231));
	plot(avgImage);
	
	cData = sweep(data, 1, mean);
	
	cv = cov(cData);
	
	e = eigen(cv);

	e_v = e$vectors;
	
	faces = matrix(NA, nrow=45045, ncol=10);
	i = 1;
	for (i in 1:10) {
		faces[,i] = cData %*% e_v[,i];
		f = norm(faces[,i], type="2");
		faces[,i] = faces[,i]/f;
		filename=paste('eigen face ', i, '.png', sep='')
		png(filename);
		plot(pixmapGrey(matrix(faces[,i], nrow=231)));
		dev.off();
	}
}

