#import required packages
import ccdproc
from os import listdir

bias_hdu = ccdproc.CCDData.read('data_bias/master_bias.fits', unit='adu')
flat_hdu_i = ccdproc.CCDData.read('data_flat/i/master_flat.fits', unit='adu')
flat_hdu_v = ccdproc.CCDData.read('data_flat/v/master_flat.fits', unit='adu')



#Band I
subtracted_flat_i = flat_hdu_i
names_i = listdir('./data_obj/i/')
images_i = [ccdproc.CCDData.read('data_obj/i/'+i, unit='adu') for i in listdir('./data_obj/i')]

for i in range(len(names_i)):
	subt_obj = ccdproc.subtract_bias(images_i[i], bias_hdu)
	corr_obj = ccdproc.flat_correct(subt_obj, subtracted_flat_i, min_value=0.000000001)
	corr_obj.write('./data_corr/i/'+names_i[i])
	subt_obj.write('./data_biascorr/i/'+names_i[i])


#Band V
subtracted_flat_v = flat_hdu_v
names_v = listdir('./data_obj/v/')
images_v = [ccdproc.CCDData.read('data_obj/v/'+i, unit='adu') for i in listdir('./data_obj/v')]


for i in range(len(names_v)):
	subt_obj = ccdproc.subtract_bias(images_v[i], bias_hdu)
	corr_obj = ccdproc.flat_correct(subt_obj, subtracted_flat_v, min_value=0.000000001)
	corr_obj.write('./data_corr/v/'+names_v[i])
	subt_obj.write('./data_biascorr/v/'+names_v[i])