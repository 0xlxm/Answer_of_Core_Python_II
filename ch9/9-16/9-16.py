#! /usr/bin/env python

def breakline(line, fd, length):
    ''' break line whose length exceed 80 '''
    pos = pos1 = 0
    num = len(line) // 80

    for i in range(num):
        start = min(80*i,pos1+1) 
        end = start + 80
        try:
            pos = line.rindex(' ', start, end)
            pos1 = pos
            fd.seek(length + pos)
            fd.write('\n')
        except ValueError, e:
            return `e`
        except IOError, e:
            return `e`

def main():
    ''' main function '''
    length = 0
    filename = raw_input('enter filename: ')
    try:
        f = open(filename, 'r+')
        allines = f.readlines()
    except IOError, e:
        print e
        return
    else:
        for l in allines:
            length += len(l)
            if len(l) > 80:
                #length -= len(l)
                retVal = breakline(l, f, length - len(l))
                if retVal != None:
                    print retVal
                    f.close()
                    break
            else:
                continue
        else:
            f.close()

if __name__ == '__main__':
    main()
