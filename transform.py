from collections import OrderedDict

def transform(data):
    #TODO: transform data

    headers = []
    data_array = []
    for key, value in data.items():
        headers.append(key)
        data_array.append(value)

    return data_array, headers