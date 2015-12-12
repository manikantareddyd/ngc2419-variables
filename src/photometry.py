from astropy.io import fits
from photutils import CircularAperture
from photutils import aperture_photometry
from math import log10
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import pdb

slope_i = 0
slope_v = 0

ngc = SkyCoord(["07h38m08.51s +38d52m54.9s"])
myObs = EarthLocation(lat=32.779444*u.deg, lon=78.964167*u.deg, height=4500*u.m)

#I Band
#These will be the list of 'list' of coordinates and radius of stars of interest
nameFile = open('dates_i.csv','r').readlines()
timeDict = {}

for i in nameFile:
	entries = i.rstrip().split(',')
	timeDict[entries[0]] = (float(entries[2]), entries[1])

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
		thisMag = -2.5*log10(float(phot_table['aperture_sum'])/float(fits.open('data_obj/i/'+key)[0].header['EXPTIME']))+10

		time = Time(timeDict[key][1])
		altaz = ngc.transform_to(AltAz(obstime = time, location = myObs))

		secZenAngle = altaz.secz

		finalMag = thisMag - float(secZenAngle)*slope_i
		thisLine = str(timeDict[key][1]) + ',' + str(timeDict[key][0]) + ',' + str(finalMag) + '\n'
		outfile.write(thisLine)

	outfile.close()


# V Band
#These will be the list of 'list' of coordinates and radius of stars of interest
nameFile = open('dates_v.csv','r').readlines()
timeDict = {}

for i in nameFile:
	entries = i.rstrip().split(',')
	timeDict[entries[0]] = (float(entries[2]), entries[1])

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
		thisMag = -2.5*log10(float(phot_table['aperture_sum'])/float(fits.open('data_obj/v/'+key)[0].header['EXPTIME']))+10

		time = Time(timeDict[key][1])
		altaz = ngc.transform_to(AltAz(obstime = time, location = myObs))

		secZenAngle = altaz.secz

		finalMag = thisMag - float(secZenAngle)*slope_v
		thisLine = str(timeDict[key][1]) + ',' + str(timeDict[key][0]) + ',' + str(finalMag) + '\n'
		outfile.write(thisLine)

	outfile.close()
