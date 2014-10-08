#!/usr/bin/env python

import json
from operator import itemgetter

CITIBIKE_FILE = 'citibike.json'
OUTPUT_FILE = 'citibike.csv'

def main(input_file=CITIBIKE_FILE, output_file=OUTPUT_FILE):
    """Parses json object from input file, creates output csv."""

    with open(input_file, 'r') as f:
        data = json.load(f)

    stations = data['stationBeanList']

    fields = ('id', 'stationName', 'stAddress1', 'stAddress2',
        'latitude', 'longitude', 'availableBikes', 'availableDocks',
        'totalDocks', 'statusValue', 'statusKey', 'testStation')

    output_fields = ('id', 'name', 'addr1', 'addr2', 'lat', 'lon',
        'bikes_avail', 'spots_avail', 'spots_total', 'status',
        'status_key', 'test_stn')

    with open(output_file, 'w') as g:
        g.write(','.join(output_fields) + '\n')

        for stn in stations:
            try:
                output = itemgetter(*fields)(stn)
                g.write(','.join(map(str, output)) + '\n')
            except:
                pass


if __name__ == '__main__':
    main()

# note: json.load() takes an open file handle (to a valid json file) as its argument
#       you can validate your json input using a tool such as www.jsonlint.com
