
#! /bin/python

def gather_info():
    height=float(raw_input('what is ur height?'))
    weight=float(raw_input('what is your weight'))
    until=raw_input('us use metric or imperial').lower().split()
    return (height,weight,until)

def bmi_calclulate(height,weight,until='m'):
         if until[0]=='m':
             size =height*weight
             print('size %s' %size)
         elif until[0]=='i':
             size =height*weight*2
             print('size %s' %size)
   #      break
   #   else:
    #       gather_info():     */
while True :
          height,weight,until=gather_info()
          if (until[0]=='m'):
              bmi_calclulate(height,weight,until='m')
              break
          elif (until[0]=='i'):
              bmi_calclulate(height,weight,until='i')
              break
          else: print (renter)
