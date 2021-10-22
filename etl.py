# Importing the required modules 
import os
import sys
import pandas as pd
from extract import extract
from transform import transform
   
out_file = "adopt-a-stream-georgia-data.csv"

# get the list of html files
os.chdir("./responses")
files = [file_name for file_name in os.listdir() if file_name.contains(".html")]
os.chdir("..")

# load a data frame with all the field names, xpaths, and elements from the csv.
html_elements = pd.read_csv("AAS-data-fields-from-html.csv")

def get_xpath(x):
    x = x.replace('//*[@id="', '')
    x = x.split('"]')
    return(x)

html_elements["XPath"] = html_elements["XPath"].apply(get_xpath)

# get one row of data from each file and append
data = []

for file in files:
    row, _ = transform(extract(file, html_elements))
    data.append(row)

# get the header and load the data into a dataframe and out to csv
_, list_header = transform(extract(files[0]))
dataFrame = pd.DataFrame(data = data, columns = list_header)
dataFrame.to_csv(out_file)
