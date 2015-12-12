from os import listdir
from astropy.io import fits
import pdb

imghdr_i = [(i, fits.open('data_obj/i/'+i)[0].header) for i in listdir('data_obj/i')]
imghdr_v = [(i, fits.open('data_obj/v/'+i)[0].header) for i in listdir('data_obj/v')]

outfile_i = open('dates_i.csv', 'w+')
outfile_v = open('dates_v.csv', 'w+')

for i in imghdr_i:
	
	t = i[1]['UT']
	h = int(t)
	t = 60*(t % h)
	m = int(t)
	t = 60*(t % m)
	s = t

	thisLine = str(i[0]) + ',' + str(i[1]['DATE-OBS']) + ' ' + str(h) + ":" + str(m) + ":" + str(s) + "," + str(i[1]['TM_START']) + ',' + str(i[1]['TM_END']) + '\n'
	outfile_i.write(thisLine)

for i in imghdr_v:
	
	t = i[1]['UT']
	h = int(t)
	t = 60*(t % h)
	m = int(t)
	t = 60*(t % m)
	s = t

	thisLine = str(i[0]) + ',' + str(i[1]['DATE-OBS']) + ' ' + str(h) + ":" + str(m) + ":" + str(s) + "," + str(i[1]['TM_START']) + ',' + str(i[1]['TM_END']) + '\n'
	outfile_v.write(thisLine)
