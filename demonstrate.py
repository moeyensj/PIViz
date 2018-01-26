import piviz as pv
import glob
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

nrg=[477.5,612.9,748.4,865.8,960.3]
ephot = 1./np.array(nrg)


data={filt:fits.open('../temptemp/{}horse.fits'.format(filt))[0] for filt in 'grizy'}
etimes = [data[filt].header['EXPTIME'] for filt in 'grizy']
print(etimes)
for j,filt in enumerate('grizy'):
    data[filt].data = data[filt].data/etimes[j]*nrg[j]



colors = ((202,0,32),(244,165,130),(247,247,247),(146,197,222),(5,113,176))
colors2 = ((228,26,28),(55,126,184),(77,175,74),(152,78,163),(255,127,0))
#colors3 = ((228,26,28),(55,126,184),(77,175,74),(152,78,163),(255,127,0))



pm,b = pv.generate_probmatrix(data,'grizy')
filterlist = 'grizy'
brightness=np.zeros((data[filterlist[0]].data.shape[0],data[filterlist[0]].data.shape[1]))
for filt in data:
    brightness+=data[filt].data
probmatrix=np.zeros((data[filterlist[0]].data.shape[0],data[filterlist[0]].data.shape[1],len(filterlist)))
for i,filt in zip(range(len(filterlist)),filterlist):
    probmatrix[:,:,i]=(data[filt].data/brightness)

#image=np.zeros((probmatrix.shape[0],probmatrix.shape[1],3))
#
#idx = np.argmax(probmatrix,axis=2)

import matplotlib.patches as mpatches

patches = []
for j,c in enumerate('grizy'):
    patches.append(mpatches.Patch(color=np.array(colors2[j])/255., label='{}'.format(c)))
plt.legend(handles=patches)

#for i in range(image.shape[0]):
#    for j in range(image.shape[1]):
#        image[i,j,:] = colors3[idx[i,j]]
#
#plt.imshow(image)
#plt.show()


#make a single image colored by most probable:
pv.make_image_series(pm,colors=colors2,output_dir='.',nimages=500)
