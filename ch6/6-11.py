#!/usr/bin/env python 
## -*- coding: UTF-8 -*- 
## Author: 
 
def int2ip(myNumber): 
    dotBitIP = '' 
    for dotBit in xrange(3,-1,-1): 
        dotBitIP = dotBitIP + str(myNumber / (256 ** dotBit)) + "." 
        if dotBit == 3 and int(dotBitIP.rstrip('.')) > 255: 
            print "Invalid IP,please enter another number ..." 
            sys.exit(1) 
        #print dotBit,dotBitIP 
        myNumber = myNumber % (256 ** dotBit) 
    return(dotBitIP.rstrip('.')) 
 
def ip2int(num):   
    ipList = num.split('.')
    for sip in ipList:
        if int(sip) > 255:
            return -1
    hexs = ''.join([hex(int(ipList[i]))[2:] for i in xrange(4)])
    return eval('0x' + hexs)

if __name__ == "__main__": 
    import sys 
    #myNumber = int(sys.argv[1]) 
    #print int2ip (myNumber) 
    print sys.argv[1]
    print ip2int(sys.argv[1]) 
