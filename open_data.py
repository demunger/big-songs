import glob
from hdf5 import *


'''
File to open sample songs data and access attributes through hdf5 getters

'''
#change this to the dir where your data is
files = glob.glob("../samples/*.h5")

hottness_counter = 0
no_files = 0
for f in files:
    h5 = open_h5_file_read(f)
    hot = get_artist_hotttnesss(h5)
    hottness_counter += hot
    no_files += 1
    h5.close()

avg_hottness = round(hottness_counter / no_files, 5)

print 'AVERAGE HOTTNESS FOR THESE SONGS IS %f' % avg_hottness