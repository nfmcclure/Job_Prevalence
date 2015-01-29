##--------------------------------------------------
##
##  Indeed API Job data retrieval script
##
##
##
##--------------------------------------------------

import urllib2
from lxml import etree

######
# Define XML Parameters
publisher_id = '6574468093927382'
v = '2'
format = 'json'
callback = ''
q = 'data+scientist' # QUERY
location = ''
sort = ''
radius = ''
st = 'jobsite'
jt = ''
start = 0
limit = '51' # NOT EMPTY
fromage = '60'
highlight = '0'
filter = '1'
latlong = '1'
co = 'us'
chnl = ''
userip = '1.2.3.4'
useragent = 'Mozilla/%2F4.0%28Firefox%29'

xml_string = 'http://api.indeed.com/ads/apisearch?publisher=' + publisher_id + '&q=' + q +'&l=' + location +\
             '&sort=' + sort + '&radius=' + radius + '&st=' + st + '&jt=' + jt + '&start=' + str(start) +\
             '&limit=' + limit + '&fromage=' + fromage + '&filter=' + filter + '&latlong=' + latlong +\
             '&co=' + co + '&chnl=' + chnl + '&userip=' + userip + '&useragent=' + useragent + '&v=' + v

job_xml = urllib2.urlopen(xml_string).read()
job_tree = etree.HTML(job_xml)

[num_results] = job_tree.xpath('//totalresults/text()')
num_results = min(int(num_results), int(limit))

city_list = []
state_list = []
snippet_list = []
lat_list = []
long_list = []
date_list = []

for p in range(0, num_results, 25):
    print('Retrieving records from page '+ str(p/25 + 1) +' out of '+ str(len(range(0,num_results,25))) +' pages.')
    start = p

    xml_string = 'http://api.indeed.com/ads/apisearch?publisher=' + publisher_id + '&q=' + q +'&l=' + location +\
             '&sort=' + sort + '&radius=' + radius + '&st=' + st + '&jt=' + jt + '&start=' + str(start) +\
             '&limit=' + limit + '&fromage=' + fromage + '&filter=' + filter + '&latlong=' + latlong +\
             '&co=' + co + '&chnl=' + chnl + '&userip=' + userip + '&useragent=' + useragent + '&v=' + v

    job_xml = urllib2.urlopen(xml_string).read()
    job_tree = etree.HTML(job_xml)

    r_index = min(25,num_results - p)

    for r in range(r_index):
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
