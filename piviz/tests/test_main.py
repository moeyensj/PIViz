import os
import glob
import numpy as np
import astropy.io.fits as fits

from piviz import generate_probmatrix
from piviz import make_image_series

IMAGE_DIR = "tests/images/"

def test_make_image():
    test_dir = os.path.join(os.path.abspath("."), IMAGE_DIR)
    data={filt:fits.open(os.path.join(test_dir, '{}horse.fits'.format(filt)))[0] for filt in 'grizy'}
    #print(data)
    for filt in data:
        data[filt].data[np.isnan(data[filt].data)] = np.nanmin(data[filt].data)
        data[filt].data = data[filt].data[:,:1840]
        #data[filt].data = data[filt].data - np.min(data[filt].data)
        #print(np.nanmin(data[filt].data))
        #print(np.nanmax(data[filt].data))


    pm = generate_probmatrix(data)
    make_image_series(pm, nimages=10, output_dir=test_dir)
    images = glob.glob(os.path.join(test_dir, "*.png"))
    assert len(images) == 10

    for im in images:
        os.remove(im)
