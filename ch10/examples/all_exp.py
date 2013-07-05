#! /usr/bin/env python

try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
#except KeyboardInterrupt:
    print 'ctrl c'
    #raise
except Exception, e:
    print 'exit', e
except BaseException, e:
    print 'base', e
