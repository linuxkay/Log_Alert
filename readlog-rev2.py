#!/usr/bin/env/python
#this python program read log file. Notify when specific word found n time
import re
file = "/tmp/access.log"
def grab_ip(file):
    ips = []
    occurence = {}
    with open (file) as file:
        for ip in file:
            ip_data=re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',ip)
            for i in ip_data:
                ips.append(i)
        for ipaddr in ips:
            if ipaddr in occurence:
                occurence[ipaddr] = occurence[ipaddr] + 1
            else:
                occurence[ipaddr] = 1
    for key, value in occurence.iteritems():
        print key, value
    return None
print grab_ip('data')


visitors = dict()
# this should be same for each line
line = '95.11.113.x - [15/Nov/2013]'
ip = line.split(" - ")[0]  # assuming it must have " - " in line
visitors[ip] = line

# finally when you are done with above things
for visitor in visitors:
        print visitors[visitor]
