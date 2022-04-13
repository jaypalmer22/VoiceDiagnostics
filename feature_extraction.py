import opensmile
import audb
#import audiofile

import pandas as pd 
import numpy as np 

import os
import time



#file = os.path.join(db.root, db.files[0])
#signal, sampling_rate = audiofile.read(file, duration=10, always_2d=True)

smile = opensmile.Smile(
	feature_set=opensmile.FeatureSet.eGeMAPSv02,
	feature_level=opensmile.FeatureLevel.Functionals,
)

for i in range(1, 209):
	filename = 'voices/' 'voice' + str(i) + '.wav'
	y = smile.process_file(filename)
	with pd.ExcelWriter('featuresv1.xlsx', mode='a', if_sheet_exists="overlay") as writer:
		y.to_excel(writer, startrow = 3 * (i - 1))

	print(i / 208 * 100, "%")









