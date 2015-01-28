##--------------------------------------------------
##
##  Indeed API Job data retrieval script
##
##
##
##--------------------------------------------------

import urllib.request
from lxml import etree

######
# Define XML Parameters
publisher_id = '6574468093927382'
v = '2'
format = 'json'
callback = ''
q = 'java' # QUERY
location = ''
sort = ''
radius = ''
st = 'jobsite'
jt = ''
start = '' # Default 0, only displays 25, so must cycle through until done.  How to find done?
limit = '20' # NOT EMPTY
fromage = '30'
highlight = '0'
filter = '1'
latlong = '1'
co = 'us'
chnl = ''
userip = '1.2.3.4'
useragent = 'Mozilla/%2F4.0%28Firefox%29'

xml_string = 'http://api.indeed.com/ads/apisearch?publisher=' + publisher_id + '&q=' + q +'&l=' + location +\
             '&sort=' + sort + '&radius=' + radius + '&st=' + st + '&jt=' + jt + '&start=' + start +\
             '&limit=' + limit + '&fromage=' + fromage + '&filter=' + filter + '&latlong=' + latlong +\
             '&co=' + co + '&chnl=' + chnl + '&userip=' + userip + '&useragent=' + useragent + '&v=' + v

job_xml = urllib.request.urlopen(xml_string).read()
job_tree = etree.HTML(job_xml)

city_list = []
state_list = []
snippet_list = []
lat_list = []
long_list = []
date_list = []

for r in range(int(limit)):
    try:
        result_tag = job_tree.xpath('//result')[r]
    except:
        city_list.append('')
        state_list.append('')
        snippet_list.append('')
        lat_list.append('')
        long_list.append('')
        city_list.append('')

    try:
        city_list.append(result_tag.find('city').text)
    except:
        city_list.append('')

    try:
        state_list.append(result_tag.find('state').text)
    except:
        state_list.append('')

    try:
        snippet_list.append(result_tag.find('snippet').text)
    except:
        snippet_list.append('')

    try:
        lat_list.append(result_tag.find('latitude').text)
    except:
        lat_list.append('')

    try:
        long_list.append(result_tag.find('longitude').text)
    except:
        long_list.append('')

    try:
        date_list.append(result_tag.find('date').text)
    except:
        date_list.append('')

print(lat_list)
print(date_list)
