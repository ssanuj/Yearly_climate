import requests
import re
import numpy as np
import pandas as pd
"""
download the data from url and create a new file wih data starting from line 7
"""
url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"
r = requests.get(url)
open('tmp.txt','wb').write(r.content)
with open('tmp.txt','r') as fo:
	#print(file.read())
	op = ''
	count = 1
	for x in fo.read().split('\n'):  
		#print(x)
		if count > 7:
			opf = open('new_file.txt', 'w')
			op = op + '\n' + x
			opf.write(op)
			opf.close()
		count+=1

#reshape = np.genfromtxt('new_file.txt',dtype=float)
#temp2 = np.transpose(reshape)
#np.savetxt('climate.txt', (temp2))
fmt =pd.read_csv('new_file.txt', delimiter=' ' header=None)



    		
    		


    
 
