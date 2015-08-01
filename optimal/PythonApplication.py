#!/usr/bin/env python
import requests


SUBDOMAIN='speedchecker'
API_ACCESS_KEY='91GdFW61a9ADq9y1PrQu'

incidents_file = open("incidents.txt","w")
print incidents_file

def get_incidents():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        'since':'2014-10-01',
        'until':'2014-12-31',
        'sort_by':'created_on:asc',
        # 'limit':20,
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/incidents'.format(SUBDOMAIN),
                    headers=headers,
                    params=payload,
    )
    print r.status_code
    # print r.text
    incidents_file.write(r.text)
    incidents_file.close()
    return incidents_file
get_incidents()
