import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors_limz.npy')
    cmap = plt.get_cmap('YlOrRd')

    u_g = data['u'] - data['g']
    r_i = data['r'] - data['i']

    redshift = data['redshift']

    plot = plt.scatter(u_g, r_i, s=0.5, lw=0, c=redshift, cmap=cmap)

    cb = plt.colorbar(plot)
    cb.set_label('Redshift')

    plt.xlabel('Colour index  u-g')
    plt.ylabel('Colour index  r-i')
    plt.title('Redshift (colour) u-g versus r-i')

    plt.xlim(-0.5, 2.5)
    plt.ylim(-0.5, 1)

    plt.show()