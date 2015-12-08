from astropy.io import fits
from os import listdir
import reproject 
import montage_wrapper as montage
names_i = listdir('./data_corr/i')
names_v = listdir('./data_corr/v')

base_i = names_i[0]
base_v = names_v[0]

ins_i = ['./data_corr/i/'+i for i in names_i]
ins_v = ['./data_corr/v/'+i for i in names_v]

outs_i = ['./data_align/i/'+i for i in names_i]
outs_v = ['./data_align/v/'+i for i in names_v]

montage.reproject(ins_i,outs_i,header=0)