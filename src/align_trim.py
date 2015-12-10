from astropy.io import fits
import ccdproc
from os import listdir
import numpy as np

images = listdir('./data_align/i')
for i in images:
	img = ccdproc.CCDData.read('./data_align/i/'+i, unit='adu')
	trimmed = ccdproc.trim_image(img,fits_section='[50:1500, 100:1500]')
	trimmed.write('./data_final/i/'+i)

images = listdir('./data_align/v')
for i in images:
	img = ccdproc.CCDData.read('./data_align/v/'+i, unit='adu')
	trimmed = ccdproc.trim_image(img,fits_section='[50:1500, 100:1500]')
	trimmed.write('./data_final/v/'+i)