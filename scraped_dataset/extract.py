import os
import sys
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd


def get_field(soup_in, field_in):
    # print("FIELD_IN =  " + str(type(field_in)))
    # print(str(field_in))
    xpath = field_in["XPath"].values[0]
    if xpath[1] == '':
        element = soup_in.find(id=xpath[0])
        if (element.get("checked") is not None) or (element.get("type") in ["radio", "checkbox"]):
            value = element.get("checked")
            if value == "checked":
                value = True
            else:
                value = False
        elif element.get("value") is not None:
            value = element.get("value")
        else:
            value = element.text
        return value
    else:
        # TODO: handle case where xpath is two-part
        return ''
    
    # TODO: handle determining what part of the element contains the data


def extract(html_file_in, html_elements):
    starting_dir = os.getcwd()
    responses_dir = starting_dir + "\\responses\\responses"
    os.chdir(responses_dir)
    with open(html_file_in) as f:
        file_content = f.read()
        soup = BeautifulSoup(file_content, 'html.parser')
    os.chdir(starting_dir)
    # build array with extracted data
    data = OrderedDict()
    for n in range(len(html_elements["XPath"].values)):    
        field = html_elements.iloc[[n]]
        # print("FIELD = " + str(field))
        data[str(field["Field Name"].values[0])] = get_field(soup, field)    
    return data
