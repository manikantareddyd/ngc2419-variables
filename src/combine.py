from astropy.io import fits
from astropy import units as u
from ccdproc import combiner
import ccdproc
from os import listdir
import numpy as np
import pdb

print "Combining..."

# All images: biases
images = [ccdproc.CCDData.read('data_bias/'+i, unit='adu') for i in listdir('./data_bias')]

c_images = combiner.Combiner(images)
master_bias = c_images.average_combine()

master_bias.write('data_bias/master_bias.fits')

# All images: flats i
images = [ccdproc.CCDData.read('data_flat/i/'+i, unit="adu") for i in listdir('./data_flat/i/')]
sub_images = [ccdproc.subtract_bias(i,master_bias) for i in images]
c_images = combiner.Combiner(sub_images)
c_images.scaling = [1/float(fits.open('data_flat/i/'+i)[0].header["EXPTIME"]) for i in listdir("./data_flat/i")]
master_flat_i = c_images.average_combine()
master_flat_i.data = master_flat_i.data/np.ma.average(master_flat_i.data)
master_flat_i.write('data_flat/i/master_flat.fits')

# All images: flats v
images = [ccdproc.CCDData.read('data_flat/v/'+i, unit="adu") for i in listdir('./data_flat/v/')]
sub_images = [ccdproc.subtract_bias(i,master_bias) for i in images]
c_images = combiner.Combiner(sub_images)
c_images.scaling = [1/float(fits.open('data_flat/v/'+i)[0].header["EXPTIME"]) for i in listdir("./data_flat/v")]
master_flat_v = c_images.average_combine()
master_flat_v.data = master_flat_v.data/np.ma.average(master_flat_v.data)
master_flat_v.write('data_flat/v/master_flat.fits')



# c_images = combiner.Combiner(images)
# c_images.scaling = lambda arr: 1/np.ma.average(arr)
# master_flat_v = c_images.average_combine()

# master_flat_v.write('data_flat/v/master_flat.fits')
