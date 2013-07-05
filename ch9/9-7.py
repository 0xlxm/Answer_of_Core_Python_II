#! /usr/bin/env python

services = open('/etc/services').readlines()
for f in services:
    print f.split('\t')
