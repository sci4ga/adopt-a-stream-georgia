# TODO: add comments
# Importing the required modules 
import os
import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

path_pre = 'https://aas.gaepd.org/Submission.aspx?Event='
event_num = 1 #TODO: why is record 88207 causing server error?
path_post = '&Mode=V'

recent = False
empty_file = "EMPTY.txt"
error_file = "ERROR.txt"
empty_count = 0

expected = 89010

roll_len = 5
rolling_time = [0] * roll_len

if(not os.path.exists("responses")):
    os.mkdir("responses")

os.chdir("responses")
s = requests.Session()

while((recent == False) or (empty_count < 10)):
    start = time.time()
    path = path_pre + str(event_num).zfill(5) + path_post
    need_response = True
    while(need_response):
        try:
            response = s.get(path)
            need_response = False
        except:
            time.sleep(30)
    response = s.get(path)
    soup = BeautifulSoup(response.content,'html.parser')
    try:
        txtDate = soup.find_all(id='txtDate')[0].get("value")

        if (type(txtDate) is str):
            file_name = str(event_num).zfill(5) + ".html"
            with open(file_name, "w") as file:
                file.write(response.text)
            dto = datetime.strptime(txtDate, '%m/%d/%Y')
            if datetime.today() - dto < timedelta(7):
                recent = True
            empty_count = 0
        else:        
            with open(empty_file, "a") as file:
                file.write( str(event_num) + "\n")
            empty_count = empty_count + 1
    except:
        with open(error_file, "a") as file:
            file.write( str(event_num) + "\n")
    
    event_num = event_num + 1
    end = time.time()
    rolling_time[event_num % roll_len] = end - start
    sum = 0
    for measurement in rolling_time:
        sum = sum + measurement
    remaining_time = (sum / roll_len) * (expected - event_num)
    remaining_time = timedelta(seconds=remaining_time)
    print(str(event_num).zfill(5) + " - Estimated time remaining: " + str(remaining_time))

print("DONE")
