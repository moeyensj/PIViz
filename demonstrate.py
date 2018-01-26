import piviz as pv
import glob
import astropy.io.fits as fits


data={filt:fits.open('../temptemp/{}whirl.fits'.format(filt))[0] for filt in 'grizy'}

pm,b = pv.generate_probmatrix(data,'grizy')
pv.make_image_series(pm,output_dir='.',nimages=10)
