import priviz as pv
import astropy.io.fits as fits
import numpy as np




data={filt:fits.open('{}horse.fits'.format(filt))[0] for filt in 'grizy'}
print(data)
for filt in data:
    data[filt].data[np.isnan(data[filt].data)] = np.nanmin(data[filt].data)
    data[filt].data = data[filt].data[:,:1840]
    #data[filt].data = data[filt].data - np.min(data[filt].data)
    print(np.nanmin(data[filt].data))
    print(np.nanmax(data[filt].data))


pm = pv.generate_probmatrix(data)
pv.make_image_series(pm,nimages=10,output_dir='./')
