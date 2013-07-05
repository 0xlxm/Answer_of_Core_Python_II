#/usr/bin/env python

"""Compress a file using a compressor object."""

import zlib, bz2, os

def compDecomp( compObj, srcName, dstName ):
    source= file( srcName, "r" )
    dest= file( dstName, "w" )
    block= source.read( 2048 )
    while block:
        cBlock= compObj.compress( block )
        dest.write(cBlock)
        block= source.read( 2048 )
    cBlock= compObj.flush()
    dest.write( cBlock )
    source.close()
    dest.close()

compObj1= zlib.compressobj()
compDecomp( compObj1, "test", "test.gz" )
print "source", os.stat("test").st_size/1024, "k"
print "dest", os.stat("test.gz").st_size/1024, "k"

compObj2= bz2.BZ2Compressor()
compDecomp( compObj2, "test", "test.bz" )
print "source", os.stat("test").st_size/1024, "k"
print "dest", os.stat("test.bz").st_size/1024, "k"
