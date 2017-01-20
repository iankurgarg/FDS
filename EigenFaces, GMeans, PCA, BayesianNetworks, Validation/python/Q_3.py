from sklearn.cluster import KMeans;
from sklearn.preprocessing import scale;
from statsmodels.stats.diagnostic import normal_ad as ad;
import numpy as np;
import matplotlib.pyplot as plt;
from matplotlib import gridspec;
from matplotlib.patches import Ellipse
import pandas;
import random;

def Gmeans (X, alpha=0.0001, k=1):
#    random.seed(1);
    KM = KMeans(n_clusters=k);
    C = KM.fit(X);
    C1 = C.cluster_centers_;
    C2 = np.vstack((C1, C1));


    while (C1.shape[0] != C2.shape[0]):
        KM = KMeans(n_clusters=C1.shape[0], init=C1);
        res = KM.fit(X);
        C2 = res.cluster_centers_;

        subX = X[res.labels_ == 0];
        C1 = SubGMeans(subX, alpha, C2[0]);
        i = 1;
        for i in range(1,C2.shape[0]):
            subX = X[res.labels_ == i];
            C3 = SubGMeans(subX, alpha, C2[i]);
            C1 = np.vstack((C1, C3));


    KM = KMeans(n_clusters=C1.shape[0], init=C1);
    res = KM.fit(X);
    C = res.cluster_centers_;

    print(res.cluster_centers_.shape[0])
    plot3d(res, X);
#    return np.array(res.cluster_centers_, dtype=float);
    return res;


def SubGMeans (x, alpha, c):
#    random.seed(1);
    KM1 = KMeans(n_clusters=1);
    c = KM1.fit(x).cluster_centers_;
    KM = KMeans(n_clusters=2);
    C = KM.fit(x);
    cc = C.cluster_centers_;

    c1 = cc[0];
    c2 = cc[1];

    v = c1 - c2;
    v = v[np.newaxis].transpose();

    modV = np.linalg.norm(v);
    if x.shape[1] > 1:
        projectedX = np.matrix(x) * v;
        projectedX = projectedX / modV;
    else:
        projectedX = np.matrix(x);

    scaledX = np.array(scale(projectedX));

    ad2, p = ad(scaledX);

    if (p < alpha):
        return cc;
    else:
        return c;


def plot3d (C, X):
    if (type(X) == pandas.core.frame.DataFrame):
        X = X.as_matrix();
    cc = C.cluster_centers_;
    d = cc.shape[1];
    if (d >= 2):
        ds = int(np.sqrt(d));
        if (ds * ds == (d * (d - 1) / 2)):
            gs = gridspec.GridSpec(ds, ds);
        elif ((ds+1)*ds > (d*(d-1)/2)):
            gs = gridspec.GridSpec(ds+1, ds);
        else:
            gs = gridspec.GridSpec(ds + 1, ds+1);

        #plt.figure();
        k = 0;
        for p in range(d):
            for q in range(d):
                if (p < q):
                    s = [p,q];
                    #plt.subplot(gs[k]);
                    plt.figure()
                    k = k+1;
                    plt.scatter(X[:, p], X[:, q], c=C.labels_);
                    plt.title("Clusters");
                    plt.xlabel("X"+str(p));
                    plt.ylabel("X"+str(q));
                    plt.scatter(cc[:,p],cc[:,q], marker='o', c="b");

                    i = 0;
                    for i in range(C.cluster_centers_.shape[0]):
                        subX = X[C.labels_ == i,][:,s];
                        cov = np.cov(subX.transpose());
                        evals, evecs = np.linalg.eig(cov);
                        e1 = Ellipse(xy=np.mean(subX, axis=0), width=4 * np.sqrt(evals[0]),
                                     height=4 * np.sqrt(evals[1]),
                                     angle=np.degrees(np.arctan2(*evecs[1])), facecolor="none", edgecolor="black");
                        e2 = Ellipse(xy=np.mean(subX, axis=0), width=2 * np.sqrt(evals[0]),
                                     height=2 * np.sqrt(evals[1]),
                                     angle=np.degrees(np.arctan2(*evecs[1])), facecolor="none", edgecolor="black");
                        e3 = Ellipse(xy=np.mean(subX, axis=0), width=6 * np.sqrt(evals[0]),
                                     height=6 * np.sqrt(evals[1]),
                                     angle=np.degrees(np.arctan2(*evecs[1])), facecolor="none", edgecolor="black");
                        plt.gca().add_artist(e1);
                        plt.gca().add_artist(e2);
                        plt.gca().add_artist(e3);

                    print("plotted" + str(p) + str(q));
        plt.show();



#Testing
'''
s1 = np.random.multivariate_normal([0,0], np.matrix([[10,6],[6,5]]), 1000);
s2 = np.random.multivariate_normal([10,20], np.matrix([[3,1],[1,6]]), 1000);
s3 = np.random.multivariate_normal([40,50], np.matrix([[12,11],[11,16]]), 1000);
s = np.vstack((s1, s2, s3));
s12 = np.vstack((s1, s2));

ss1 = np.random.normal(0, 10, 100)[np.newaxis].transpose();
ss2 = np.random.normal(10, 3, 100)[np.newaxis].transpose();
ss3 = np.random.normal(40, 11, 100)[np.newaxis].transpose();

ss = np.vstack((ss1, ss2, ss3));

XX = pandas.read_csv('hw45-r3b-test-data.csv');

ans = Gmeans(XX, 0.0001, 1);
print(ans.cluster_centers_.shape[0]);
'''