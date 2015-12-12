#import required packages
from astropy.io import fits
from os import listdir
from os.path import isfile, join
from os import rename
import pdb

obj_dir = 'data_obj/'
flat_dir = 'data_flat/'

obj_names = listdir(obj_dir)
flat_names = listdir(flat_dir)

obj_names.remove('i')
obj_names.remove('v')
flat_names.remove('i')
flat_names.remove('v')

obj_images = [fits.open(obj_dir+i, ignore_missing_end=True)[0].header['FILTER'] for i in obj_names]
flat_images = [fits.open(flat_dir+i, ignore_missing_end=True)[0].header['FILTER'] for i in flat_names]

#pdb.set_trace()

for i in range(len(obj_names)):
	#pdb.set_trace()
	if 'I' in obj_images[i]:
		rename(obj_dir+obj_names[i], obj_dir+'i/'+obj_names[i])
	elif 'V' in obj_images[i]:
		rename(obj_dir+obj_names[i], obj_dir+'v/'+obj_names[i])
	else:
		print 'Unknown band!'


for i in range(len(flat_names)):
	#pdb.set_trace()
	if 'I' in flat_images[i]:
		rename(flat_dir+flat_names[i], flat_dir+'i/'+flat_names[i])
	elif 'V' in flat_images[i]:
		rename(flat_dir+flat_names[i], flat_dir+'v/'+flat_names[i])
	else:
		print 'Unknown band!'

