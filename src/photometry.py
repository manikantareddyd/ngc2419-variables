from astropy.io import fits
from photutils import CircularAperture
from photutils import aperture_photometry
from math import log10

#I Band
#These will be the list of 'list' of coordinates and radius of stars of interest
nameFile = open('names_start_end_I.csv','r').readlines()
timeDict = {}

for i in nameFile:
	entries = i.rstrip().split(',')
	timeDict[entries[0]] = float(entries[1])

coordFile = open('coords_I.csv','r').readlines()
coordinates = []

for i in coordFile:
	entries = i.rstrip().split(',')
	thisCoord = [float(entries[0]), float(entries[1]), float(entries[2])]
	coordinates.append(thisCoord)

for i in range(len(coordinates)):

	outfile = open('phots/i/'+str(i)+'.csv', 'w+')

	for key in sorted(timeDict.keys(), key = str.lower):

		aperture = CircularAperture([(coordinates[i][0], coordinates[i][1])], r=coordinates[i][2])
		phot_table = aperture_photometry(fits.open('data_final/i/'+key)[0].data, aperture)
		thisLine = str(timeDict[key]) + '\t' + str(2.5*log10(float(phot_table['aperture_sum'])/float(fits.open('data_obj/i/'+key)[0].header['EXPTIME']))+10) + '\n'
		outfile.write(thisLine)

	outfile.close()


# V Band
#These will be the list of 'list' of coordinates and radius of stars of interest
nameFile = open('names_start_end_V.csv','r').readlines()
timeDict = {}

for i in nameFile:
	entries = i.rstrip().split(',')
	timeDict[entries[0]] = float(entries[1])

coordFile = open('coords_V.csv','r').readlines()
coordinates = []

for i in coordFile:
	entries = i.rstrip().split(',')
	thisCoord = [float(entries[0]), float(entries[1]), float(entries[2])]
	coordinates.append(thisCoord)

for i in range(len(coordinates)):

	outfile = open('phots/v/'+str(i)+'.csv', 'w+')

	for key in sorted(timeDict.keys(), key = str.lower):

		aperture = CircularAperture([(coordinates[i][0], coordinates[i][1])], r=coordinates[i][2])
		phot_table = aperture_photometry(fits.open('data_final/v/'+key)[0].data, aperture)
		thisLine = str(timeDict[key]) + '\t' + str(float(phot_table['aperture_sum'])) + '\n'
		outfile.write(thisLine)

	outfile.close()