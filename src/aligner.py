from astropy.io import fits
from os import listdir
from reproject import reproject_exact

names_i = listdir('./data_corr/i')
names_v = listdir('./data_corr/v')

base_i = names_i[0]
base_v = names_v[0]

outs_i = ['./data_align/i/'+i for i in names_i]
outs_v = ['./data_align/v/'+i for i in names_v]

for i in range(len(names_i)):
	array, footprint = reproject_exact(fits.open(names_i), fits.open(base_i)[0].header)
