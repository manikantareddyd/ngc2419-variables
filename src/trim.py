from astropy.io import fits
import ccdproc
from os import listdir
import numpy as np

images = listdir('./data_corr/i')
for i in images:
	img = ccdproc.CCDData.read('./data_corr/i/'+i, unit='adu')
	trimmed = ccdproc.trim_image(img,fits_section='[150:1800, 150:1800]')
	trimmed.write('./data_corr_trimmed/i/'+i)

images = listdir('./data_corr/v')
for i in images:
	img = ccdproc.CCDData.read('./data_corr/v/'+i, unit='adu')
	trimmed = ccdproc.trim_image(img,fits_section='[150:1800, 150:1800]')
	trimmed.write('./data_corr_trimmed/v/'+i)