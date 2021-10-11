import os
import sys
from bs4 import BeautifulSoup
from collections import OrderedDict

# functions for extracting fields
def get_txtSite(soup_in):
    value = soup_in.find(id="txtSite").get("value")
    return value

def get_lblGroupName(soup_in):
    value = soup_in.find(id="lblGroupName").text 
    return value


def extract(html_file_in):
    with open(html_file_in) as f:
        file_content = f.read()
        soup = BeautifulSoup(file_content, 'html.parser')
    
    # build array with extracted data
    data = OrderedDict()
    data['txtSite'] = get_txtSite(soup)
    data['lblGroupName'] = get_lblGroupName(soup)
    #TODO: extract remaining fields
    
    return data
