library(ISLR);

part1 <- function() {
  data = Default;
  data$default = factor(data$default);
  logit = glm (default ~ income + balance, data, family="binomial");
  predictions = predict(logit, type='response');
  predictions = ifelse(predictions < 0.5, 0, 1);
  test_actual = ifelse(data$default == "No", 0, 1);
  test_error = (test_actual == predictions);
  error = sum(test_error == FALSE)/length(test_error);
  print(error)
}


LOG_REG_WITH_VAL <- function () {
	data = Default;
	data$default = factor(data$default);
	
	n = dim(data)[1];
	train = sample(n, 9*n/10);

	lm.fit = glm(default ~ income + balance, data, family="binomial", subset=train)

	test_res = (predict(lm.fit, data, type='response'))[-train]

	test_result = ifelse(test_res < 0.5, 0, 1);

	test_act = data$default[-train];

	test_actual = ifelse(test_act == "No", 0, 1);

	test_error = (test_actual == test_result);

	error = sum(test_error == FALSE)/length(test_error);

	print(error);
}

part3 <- function () {
  n = dim(data)[1];
  train = sample(n, n/2);
  lm.fit = glm(default ~ income + balance + student, data, family = "binomial", subset = train);
  test_res = (predict(lm.fit, data, type='response'))[-train];
  test_result = ifelse(test_res < 0.5, 0, 1);
  test_act = data$default[-train];
  test_actual = ifelse(test_act == "No", 0, 1);
  test_error = (test_actual == test_result);
  error = sum(test_error == FALSE)/length(test_error);
  print(error);
}