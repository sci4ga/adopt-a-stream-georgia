import os
import sys
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd


def get_field(soup_in, field):
    xpath = field["XPath"][0]
    if xpath[1] != '':
        element = soup_in.find(id=xpath[0]).get("value")
    else:
        # TODO: handle case where xpath is two-part
        element = soup_in.find(id=xpath[0]).get("value")
    
    # TODO: handle determining what part of the element contains the data
    if True:
        value = element.get("value")
    else:
        value = element.text

    return value

def extract(html_file_in, html_elements):
    with open(html_file_in) as f:
        file_content = f.read()
        soup = BeautifulSoup(file_content, 'html.parser')
    
    # build array with extracted data
    data = OrderedDict()
    for n in range(len(html_elements["XPath"].values)):    
        field = html_elements.iloc[[n]]
        data[html_elements.iloc[[n]]["Field Name"][0]] = get_field(soup, field)
    
    return data
