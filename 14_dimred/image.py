#!/usr/bin/env python
import numpy as np
import pylab as pl

from sklearn.decomposition import PCA

from ggplot import *

IMAGE_FILE = 'einstein.jpg'
def pca(A, num_pcs=0):

    # compute eigenval/eigenvec of covariance mtx
    M = (A - np.mean(A.T, axis=1)).T
    sigma = np.cov(M)
    egvals, egvecs = np.linalg.eig(sigma)

    # sort egvals (note argsort returns index mask)
    idx = np.argsort(egvals)    # desc
    idx = idx[::-1]             # asc
    egvals = egvals[idx]

    # sort egvecs
    egvecs = egvecs[:, idx]

    # truncate pc's (if necessary)
    if num_pcs < np.size(egvecs, axis=1):
        egvecs = egvecs[:, range(num_pcs)]

    # project data into lower-dim space
    proj = np.dot(egvecs.T, M)

    return egvecs, proj, egvals

def main():
    A = pl.imread(IMAGE_FILE)

    # full pca
    sk_pca = PCA()
    sk_pca.fit(A)

    # create scree plot
    expl_var = pd.DataFrame(sk_pca.explained_variance_ratio_[:20],
        columns=['pct_expl_var'])
    expl_var['index'] = range(len(expl_var))

    g = (ggplot(expl_var, aes('index', 'pct_expl_var')) + geom_point() +
        geom_line() + ggtitle('image scree plot'))
    ggsave(g, 'scree.jpg')
    
    i = 1
    pc_values = (1, 5, 10, 20, 30, 40)

    # draw approximated images
    for num_pcs in pc_values:

        # perform (truncated) pca
        egvecs, proj, egvals = pca(A, num_pcs)

        # reconstruct image
        A_rec = np.dot(egvecs, proj).T + np.mean(A, axis=0)
         
        # create subplot
        ax = pl.subplot(2, 3, i, frame_on=False)
        ax.xaxis.set_major_locator(pl.NullLocator())
        ax.yaxis.set_major_locator(pl.NullLocator())

        # draw
        pl.imshow(A_rec)
        pl.title("{} pc's".format(num_pcs))
        pl.gray()

        i += 1

    pl.show()

if __name__ == '__main__':
    main()

# adapted from
# http://glowingpython.blogspot.it/2011/07/pca-and-image-compression-with-numpy.html
