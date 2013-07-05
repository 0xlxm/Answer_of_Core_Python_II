#! /usr/bin/env python

'''
11-11. Functional Programming with map(). Write a program that takes a filename and
       "cleans" the file by removing all leading and trailing whitespace from each line. Read
       in the original file and write out a new one, either creating a new file or overwriting
       the existing one. Give your user the option to pick which of the two to perform.
       Convert your solution to using list comprehensions.
'''

#def stripWhite(alllines):
    #return [line for line in [c for l in alllines for c in l if c != ' ']]
        #return map(str.strip, alllines)
        #return [line.strip() + '\n' for line in f1]
def main():
    prompt = '''
Welcome to fileStripper!
Save the handled content to the (O)riginal file;
Save the handled content to the a (N)ew file.
Your choice: '''

    chosen = False
    choice = raw_input(prompt)[0].lower()
    if choice not in 'onq':
        print 'Invalid option, try again!'
    else:
        print '\nYou Picked: [%s]' % choice
        fname = raw_input('enter the filename to handle: ')
        try:
            f1 = open(fname, 'r+')
        except IOError, e:
            print e[1]
        else:
            stripedContent = [line.strip() + '\n' for line in f1]
            if choice == 'o':
                f1.seek(0)
                f1.truncate()
                f1.writelines(stripedContent)
                f1.close()
            elif choice == 'n':
                nf = raw_input('Enter the filename to save the striped contend: ')
                f2 = open(nf, 'w')
                f2.writelines(stripedContent)
                f2.close()
    
if __name__ == '__main__':
    main()
