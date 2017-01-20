import pandas as pd;
from sklearn import linear_model as lm;
import numpy as np;

def part1 (input):
    data = pd.read_csv(input);

    Y = data.default.to_frame();
    Y = Y.replace(["Yes","No"] , [1, 0]);

    X = data.income.to_frame();
    X['balance'] = data.balance.to_frame();

    logit = lm.LogisticRegression(penalty="l1", C=1);
    result = logit.fit(X, Y);

    predictions = logit.predict(X);

    actual = data.default;
    actual  = actual.replace(["Yes","No"] , [1, 0]);

    test_error = (actual == predictions);

    error = sum(test_error == False)/(test_error.shape[0]);
    print(error);

def LOG_REG_WITH_VAL (input) :
    data = pd.read_csv(input);

    n = data.shape[0];
    train = np.random.choice(n, int(n/2), False);
    trainData = data.iloc[train];

    Y1 = trainData.default.replace(["Yes", "No"], [1, 0]);
    Y = Y1.to_frame();
    trainX = trainData.income.to_frame();
    trainX['balance'] = trainData.balance.to_frame();

    logit = lm.LogisticRegression(penalty="l1", C=1);
    result = logit.fit(trainX, Y);

    test = np.ones((n, 1), dtype=bool);

    for i in train:
        test[i] = False;

    testData = data[test];

    testX = testData.income.to_frame();
    testX['balance'] = testData.balance.to_frame();

    predictions_test = logit.predict(testX);
    predictions_train = logit.predict(trainX);

    actual = testData.default.replace(["Yes", "No"], [1, 0]);


    train_error = (Y1 == predictions_train);
    test_error = (predictions_test == actual);


    error = sum(test_error == False)/ (test_error.shape[0]);
    print(error);


def part3 (input):
    data = pd.read_csv(input);
    n = data.shape[0];
    train = np.random.choice(n, int(n / 2), False);
    trainData = data.iloc[train];

    logit = lm.LogisticRegression(penalty="l1", C=1);

    X = trainData.income.to_frame();
    X['balance'] = trainData.balance.to_frame();
    X['student'] = trainData.student.replace(["Yes", "No"], [1, 0]).to_frame();
    Y = trainData.default.replace(["Yes", "No"], [1, 0]).to_frame();

    logit.fit(X, Y);

    test = np.ones((n, 1), dtype=bool);

    for i in train:
        test[i] = False;

    testData = data[test];

    testX = testData.income.to_frame();
    testX['balance'] = testData.balance.to_frame();
    testX['student'] = testData.student.replace(["Yes", "No"], [1, 0]).to_frame();

    predictions = logit.predict(testX);
    actual = testData.default.replace(["Yes", "No"], [1, 0]);

    test_error = (actual == predictions);
    error = sum(test_error == False) / (test_error.shape[0]);
    print(error);