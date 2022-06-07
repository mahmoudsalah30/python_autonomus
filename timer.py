#! /bin/python

import time
start_time=time.localtime()
print("start time %s" %time.strftime('%X',start_time))

raw_input('please press eneter to stop')


end_time=time.localtime()

print ('end time %s' %time.strftime('%X',end_time))

diffrence=time.mktime(end_time)-time.mktime(start_time)

print('differnce %s' %diffrence)

