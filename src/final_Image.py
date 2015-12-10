from astropy.io import fits
from astropy import units as u
from ccdproc import combiner
import ccdproc
from os import listdir
import numpy as np
import pdb

print "Combining..."


# All I
images_i = [ccdproc.CCDData.read('data_final/i/'+i, unit="adu") for i in listdir('./data_final/i/')]
c_images_i = combiner.Combiner(images_i)
master_i = c_images_i.median_combine()
master_i.write('Final_I.fits')

# All V
images_v = [ccdproc.CCDData.read('data_final/v/'+i, unit="adu") for i in listdir('./data_final/v/')]
c_images_v = combiner.Combiner(images_v)
master_v = c_images_v.median_combine()
master_v.write('Final_V.fits')
