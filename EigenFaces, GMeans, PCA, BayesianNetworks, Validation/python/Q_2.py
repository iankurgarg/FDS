import os;
import numpy as np;
import matplotlib.pyplot as plt;

def PCA( input ):
    a = os.listdir(input);
    images = [];
    w = 0;
    h = 0;

    for f in a:
        p = os.path.join(input, f);
        i = open(p, 'rb');
        i.readline();
        i.readline();
        (w, h) = [int(n) for n in i.readline().split()];
        d = int(i.readline());

        image = []
        for x in range(h):
            for y in range(w):
                image.append(ord(i.read(1)));
        images.append(image);

    images = np.matrix(images);
    images = images.transpose();

    meanImg = np.mean(images, axis = 1).transpose();
    meanImage = np.reshape(meanImg, (h, w));
    plt.imshow(meanImage.astype((int)), cmap="Greys_r");
    plt.show();

    r = images.shape;
    meanImg = meanImg.astype(int);

    for i in range(r[0]):
        images[i] = images[i] - meanImg[0,i];

    cov = np.cov(images.transpose());

    evals, evecs = np.linalg.eig(cov);

    for i in range(10):
        v1 = evecs[:, i];
        v1 = v1[np.newaxis].transpose();
        face = images * v1;
        ef = np.array(np.reshape(face, (h, w))).astype(int);
        im = plt.imshow(ef, cmap="Greys_r");
        plt.savefig("eigen face "+str(i)+".png");
        print("Face " +str(i) +" saved")

    return;
