import os
from astropy.io import fits
from astropy import visualization as aviz
import matplotlib.pyplot as plt
import numpy as np

__all__ = ["generate_image",
           "generate_probmatrix",
           "make_image_series"]

def generate_image(pmatrix,colors):
    rand_mat = np.random.rand(pmatrix.shape[0],pmatrix.shape[1])
    image=np.zeros((pmatrix.shape[0],pmatrix.shape[1],3))
    for i in range((len(colors))):
        image[(rand_mat<pmatrix[:,:,i])&~(image.any(axis=2))]=colors[i]
    return image

def generate_probmatrix(data,filterlist=['g','r','i','z','y']):
    brightness=np.zeros((data[filterlist[0]].data.shape[0],data[filterlist[0]].data.shape[1]))
    for filt in data:
        brightness+=data[filt].data
    probmatrix=np.zeros((data[filterlist[0]].data.shape[0],data[filterlist[0]].data.shape[1],len(filterlist)))
    for i,filt in zip(range(len(filterlist)),filterlist):
        cdf=probmatrix[:,:,i-1]
        probmatrix[:,:,i]=(data[filt].data/brightness)+cdf
    return probmatrix,brightness



def make_image_series(probmatrix,colors=None,brightness=None,output_dir='media/sf_LM_Shared/PIViz/',nimages=1000,basename='img'):
    #req_shape = (probmatrix.shape[0],probmatrix.shape[1],len(colors))
    #assert(len(probmatrix.shape)==3),'Probability matrix size is wrong: provided shape is {}, required shape is {}'.format(probmatrix.shape,())
    if brightness is None:
        brightness = np.ones((probmatrix.shape[:2]))
    if colors is None:
        colors=[(0,0,1),(0,1,1),(0,1,0),(1,1,0),(1,0,0)]

    for i in range(nimages):
        colorVals=generate_image(probmatrix,colors)
        plt.imshow(colorVals*brightness[:, :,np.newaxis])
        plt.savefig(os.path.join(output_dir,'{}{:03d}.png'.format(basename,i)))
        plt.clf()
        plt.close()
        if i % 10 == 0:
            print('Finished {} of {}...'.format(i+1,nimages))

