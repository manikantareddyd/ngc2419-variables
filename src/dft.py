import os

import scipy as sp
import scipy.misc
import imreg_dft as ird
from astropy.io import fits
print "Libraries imported..."

names_i = os.listdir('./data_corr_trimmed/i')
names_v = os.listdir('./data_corr_trimmed/v')
print "Directories enlisted..."

print "Entering I alignments..."
im_ref = fits.open('data_corr_trimmed/v/'+names_v[8])[0].data
for i in range (len(names_i)):
	im_test = fits.open('data_corr_trimmed/i/'+names_i[i])[0].data
	result = ird.similarity(im_ref,im_test,numiter=2)
	print i,names_i[i],"tvec:",result['tvec'],"    success:",result['success']
	out_hdu = fits.PrimaryHDU(result['timg'])
	out_hdu.writeto('data_align/i/'+names_i[i])
print "I alignments done..."

print "Entering V alignments..."
im_ref = fits.open('data_corr_trimmed/v/'+names_v[8])[0].data
for i in range (len(names_v)):
	im_test = fits.open('data_corr_trimmed/v/'+names_v[i])[0].data
	result = ird.similarity(im_ref,im_test,numiter=2)
	print i,names_v[i],"tvec:",result['tvec'],"    success:",result['success']
	out_hdu = fits.PrimaryHDU(result['timg'])
	out_hdu.writeto('data_align/v/'+names_v[i])
print "V alignments done..."