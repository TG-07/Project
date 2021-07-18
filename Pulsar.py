import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


def mean_fits(fitslist):
    n = len(fitslist)
    sum1 = 0
    data1 = []
    for x in range(n):
        hdulist = fits.open(fitslist[x])
        data = hdulist[0].data
        sum1 += data
    return sum1 / n


if __name__ == '__main__':
    data = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    print(data[100, 100])

    plt.imshow(data.T, cmap=plt.cm.cool)
    plt.colorbar()
    plt.show()