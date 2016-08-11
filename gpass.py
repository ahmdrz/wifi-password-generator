# -*- coding: utf-8 -*-
import iwlist
import sys
import getopt
import io
from random import randint

interface = ''
essid = ''
min_size = 6
salt = ['!','@','#','$','%','^','&','*','(',')']

def help(exitcode):
    print 'gpass.py -i <interface> -e <essid> [-m <minsize>]'
    sys.exit(exitcode)
    
    
def check_essid(cells,name):    
    for cell in cells:
       if cell['essid'] == essid:
           return cell
    return False

    
def generate_string(string):
    temporary_list = []
    for i in range(0,len(string)-1):
        for j in range(i+1,len(string)+1):   
            temporary_list.append(string[i:j])
    return temporary_list


def merge_arrays(arra,arrb):
    temporary_list = []
    for i in arra:
        for j in arrb:
            temporary_list.append(i+j)
            temporary_list.append(j+i)
    return temporary_list


def add_sufix(sufix,arr):
    temporary_list = []
    for i in arr:
        temporary_list.append(i+sufix)
    return temporary_list

    
def add_prefix(prefix,arr):
    temporary_list = []
    for i in arr:
        temporary_list.append(i+prefix)
    return temporary_list


if __name__ == "__main__":
   try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:e:m:",["iface=","essid=","minsize="])
   except getopt.GetoptError:
      help(2)
   for opt, arg in opts:
       if opt in ("-h","--help"):
           help(0)
       elif opt in ("-i", "--iface"):
         interface = arg
       elif opt in ("-e", "--essid"):
         essid = arg
       elif opt in ("-m", "--minsize"):
         min_size = int(arg)
   
   if len(interface) * len(essid) == 0:
       help(1)

   try:
       print 'Program started ! Scaning...'
       cells = iwlist.parse(iwlist.scan(interface))
       print ''
       cell = check_essid(cells,essid)
   
       if (cell == False):
           print 'essid not found ! try again without any connection'
           sys.exit(3)
   except:
       print "Error occured in scannig"
       sys.exit(4)
       
   try:    
       generated_list = []
       arra = generate_string(cell['mac'].replace(':',''))
       arrb = generate_string(cell['essid'])
       generated_list = merge_arrays(arra,arrb)   
    
       for pw in merge_arrays(arra,arrb):       
           for ch in salt:               
               generated_list.append(add_sufix(ch,pw))
               generated_list.append(add_prefix(ch,pw))
    
       id = randint(10000,99999)
       id = 'output' + str(id) + '.txt'
       count = 0
       with io.open(id,'a',encoding='utf8') as f:                                
           for pw in generated_list:
               item = ''
               for i in pw: #pw is unicode list , it's should be a str
                   item = item + i #how can i fix it :|
               if len(item) >= min_size:
                   count = count + 1
                   f.write(item + '\n')
                
       print 'End of program , ' + str(count) + ' generated ! codes are in ' + id       
   except:
       print 'Error occured in generating !'
       sys.exit(5)
