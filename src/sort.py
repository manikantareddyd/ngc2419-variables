#!/usr/bin/python

#import required packages
from astropy.io import fits
from os import listdir
from os.path import isfile, join
from shutil import copyfile

#all images
images = listdir('./data')

for image in images:
    try:
        #open header
        hdu = fits.open('./data/'+image,ignore_missing_end=True)
        
        #sort accordingly
        if hdu[0].header['object']=='flat':
            copyfile("./data/"+image,"./data_flat/"+image)
        elif hdu[0].header['object']=='bias':
            copyfile("./data/"+image,"./data_bias/"+image)
        elif hdu[0].header['object']=='NGC2419':
            copyfile("./data/"+image,"./data_obj/"+image)
        else:
            print "Unknown file type"
    #if error
    except IOError:
        print "Corrupt file or can't read", image
