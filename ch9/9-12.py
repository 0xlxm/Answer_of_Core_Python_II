#! /usr/bin/env python
#-*- coding: utf-8 -*-

#9-12. Users and Passwords.
#Do Exercise 7-5, which keeps track of usernames and passwords. Update your code to
#support a "last login time" (7-5a). See the documentation for the time module to
#obtain timestamps for when users "log in" to the system.
#Also, create the concept of an "administrative" user that can dump a list of all the
#users, their passwords (you can add encryption on top of the passwords if you wish [7-
#5c]), and their last login times (7-5b).
#a.
#The data should be stored to disk, one line at a time, with fields delimited by
#colons ( : ), e.g., "joe:boohoo:953176591.145", for each user. The number of
#lines in the file will be the number of users that are part of your system.
#b.
#Further update your example such that instead of writing out one line at a
#time, you pickle the entire data object and write that out instead. Read the
#documentation on the pickle module to find out how to flatten or serialize your
#file:///D|/1/0132269937/ch09lev1sec11.html (2 von 6) [13.11.2007 16:23:39]
#More free ebooks : http://fast-file.blogspot.com
#Section 9.11. Exercises
#object, as well as how to perform I/O using picked objects. With the addition of
#this new code, your solution should take up fewer lines than your solution in
#part (a).
#c.
#Replace your login database and explicit use of pickle by converting your code
#to use shelve files. Your resulting source file should actually take up fewer lines
#than your solution to part (b) because some of the maintenance work is gone.

'''
default admin password 'toot'; enjoy :)
'''
import os
import sys
import time
import random
import pickle, shelve
import signal
import crypt, string

# for c):
db = shelve.open('Userinfo_caseC', writeback=True)
if 'admin' not in db:
    db['admin'] = ['xaXKvnttUNe3A', '']

def getsalt():
    chars = './' + string.ascii_letters + string.digits
    return random.choice(chars) + random.choice(chars)

def resetpwd(name):
    if name == 'admin':
        username = raw_input('user you want to reset(defaut yourself): ')
        if username != '' and username.lower() in db:
            name = username
        else:
            print 'no such user.'

    while True:
        pwd1 = raw_input('new passwd for %s: ' % name) 
        pwd2 = raw_input('again: ')
        if pwd1 != pwd2:
            print 'inconsistent input, try again:'
            continue
        else:
            break
    pwd = crypt.crypt(pwd2, getsalt())
    db[name][0] = pwd

def delete_user():
    name = raw_input('username to delete: ')
    if name in db:
        print 'Deleted', name 
    else:
        print 'No user called', name

def login():
    print 'Welcom to xx system :)'
    name = raw_input('username: ').lower()
    #if not name in db:
    if name not in db:
        choice = raw_input("U haven't registered, register now?(y/n): ")
        if 'y' == choice:
            pwd = raw_input('enter password for %s: ' % name)
            db[name] = [] + [crypt.crypt(pwd, getsalt())]
            db[name].append(time.asctime())
    else:
        pwd = raw_input('passwd: ')
        passwd = db.get(name)[0]
        if passwd == crypt.crypt(pwd, passwd[:2]):
            if name =='admin' and db[name][1] == '':
                print db
                print 'Dear admin, this is your first time to login, please reset your passwd.'
                resetpwd(name)
            if db[name][1] != '' and time.localtime()[3] - int(db[name][1][8:10]) <= 4:
                print 'You last logged in at ', db[name][1]
            db[name][1] = time.asctime()
            print 'welcome back', name
            showmenu(name)
        else:
            print 'login incrrect'

def Print_user_info():
    print db
    if len(db) > 0:
        print 'username\tpwd\t\tLast log in'
        for name in db:
            print '%s\t\t%s\t%s' % (name, db[name][0], db[name][1])
    else:
        print 'No user at all'

def exportuser():
# for a)
#    f = open('Userinfo_caseA', 'w')
#    for l in db:
#        line = l + ':' + db[l][0] + ':' + db[l][1] + '\n'
#        f.write(line)
#    f.close()
# for b)
    f = open('Userinfo_caseB', 'w')
    pickle.dump(db, f)
    f.close()
    
def showmenu(name):
    prompt2admin = '''
(D)elete a User
(P)rint User info
(R)eset password
(E)xport User info
(S)hut down xx system
(Q)uit
Enter choice: '''
    prompt2all = '''
(R)eset password
(Q)uit
Enter choice: '''

    choices = 'dpresq' if name == 'admin' else 'rq'
    prompt = prompt2admin if name == 'admin' else prompt2all
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in choices:
                print 'invalid option, try again'
            else:
                chosen = True
                if choice == 'q': done = True 
                if choice == 'r': resetpwd(name)
                if choice == 'd': delete_user()
                if choice == 'p': Print_user_info()
                if choice == 'e': exportuser()
                if choice == 's': sys.exit(0);db.close()

def signal_handler(singal, frame):
    print '\nCtrl+C received, exit...'
    db.close()
    sys.exit(0)

if __name__ == '__main__':
    #showmenu()
#    if os.path.exists('Userinfo_caseB'):
#        f = open('Userinfo_caseB')
#        db = pickle.load(f)
#        f.close()
#    else:
#        print 'seems we lost the userinfo of lasttime'
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        login()
