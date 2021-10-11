# Importing the required modules 
import os
import sys
import pandas as pd
from extract import extract, get_list_header
from transform import transform
   
out_file = "adopt-a-stream-georgia-data.csv"
files = [] #TODO: populate array with html file names in /responses
data = []

for file in files:
    row, _ = transform(extract(file))
    data.append(row)

_, list_header = transform(extract(files[0]))
dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.to_csv(out_file) #TODO: decide on flat file format - feather? pickle?
