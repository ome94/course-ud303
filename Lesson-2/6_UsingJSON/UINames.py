#!/usr/bin/env python3
#
# Client for the UINames.com service.
#
# 1. Decode the JSON data returned by the UINames.com API.
# 2. Print the fields in the specified format.
#
# Example output:
# My name is Tyler Hudson and the PIN on my card is 4840.

import requests


def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=United%20States", # uinames API isn't working
                     timeout=2.0)                                         # at the moment
    # 1. Add a line of code here to decode JSON from the response.
    person = r.json()

    return "My name is {} {} and the PIN on my card is {}.".format(
        # 2. Add the correct fields from the JSON data structure.
        person['name'],
        person['surname'],
        person['credit_card']['pin']
    )

if __name__ == '__main__':
    print(SampleRecord())
