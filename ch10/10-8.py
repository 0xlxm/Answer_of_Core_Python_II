#! /usr/bin/env python

'''
10-8. Improving raw_input(). At the beginning of this chapter, we presented a "safe" version
    of the float() built-in function to detect and handle two different types of exceptions
    that float() generates. Likewise, the raw_input() function can generate two different
    exceptions, either EOFError or KeyboardInterrupt on end-of-file (EOF) or cancelled
    input, respectively. Create a wrapper function, perhaps safe_ input(); rather than
    raising an exception if the user entered EOF (^D in Unix or ^Z in DOS) or attempted
    to break out using ^C, have your function return None that the calling function can
    check for.
'''

def safe_raw_input(prompt):
    ''' safe version of raw_input. excluded EOFError and KeyboardInterrupt 
    exception. return None if failed '''

    try:
        result = raw_input(prompt)
    except (EOFError, KeyboardInterrupt), e:
        return None
    else: 
        return result

def main():
    retVal = safe_raw_input('Input anything: ')
    #if retVal == None:
    #    print '\nFailed!'
    #else:
    #    print retVal
    print retVal    
if __name__ == '__main__':
    main()

