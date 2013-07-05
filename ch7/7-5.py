#! /usr/bin/env python

# userpw2.py

'''
a.
Update the script so that a timestamp (see the time module) is also kept with
the password indicating date and time of last login. This interface should
prompt for login and password and indicate a successful or failed login as
before, but if successful, it should update the last login timestamp. If the login
occurs within four hours of the last login, tell the user, "You already logged in
at: <last_ login_timestamp>."

b.
Add an "administration" menu to include the following two menu options: (1)
remove a user and (2) display a list of all users in the system and their
passwords

c.
The passwords are currently not encrypted. Add password-encryption if so
desired (see the crypt, rotor, or other cryptographic modules).

d.
*Add a GUI interface, i.e., Tkinter, on top of this application.

e.
Allow usernames to be case-insensitive.

f.
Restrict usernames by not allowing symbols or whitespace.

g.
Merge the "new user" and "old user" options together. If a new user tries to log
in with a nonexistent username, prompt if they are new and if so, do the
proper setup. Otherwise, they are an existing user so log in as normal.
'''

#Last login: Thu Mar 21 11:32:51 2013 from esisop63.emea.nsn-net.net

import time
import random
import crypt, string

db = {}

def getsalt():
    chars = './' + string.ascii_letters + string.digits
    return random.choice(chars) + random.choice(chars)

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt).lower()
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = crypt.crypt(raw_input('passwd: '), getsalt())
    db[name] = [] + [pwd]
    db[name].append(time.asctime())

def olduser():
    name = raw_input('login: ').lower()
    pwd = raw_input('passwd: ')
    passwd = db.get(name)[0]
    if passwd == crypt.crypt(pwd, passwd[:2]):
        if time.localtime()[3] - int(db[name][1][8:10]) <= 4:
            print 'You already logged in at ', db[name][1]
            db[name][1] = time.asctime()
        else:
            print 'welcome back', name
    else:
        print 'login incrrect'

def delete_user():
    name = raw_input('username: ')
    if name in db:
        print 'Deleted', name 
    else:
        print 'No user called', name

def login():
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
            if time.localtime()[3] - int(db[name][1][8:10]) <= 4:
                print 'You already logged in at ', db[name][1]
                db[name][1] = time.asctime()
            else:
                print 'welcome back', name
        else:
            print 'login incrrect'

def Print_user_info():
    if len(db) > 0:
        print 'username\tpwd'
        for name in db:
            print '%s\t\t%s' % (name, db[name][0])
    else:
        print 'No user at all'

def showmenu():
    prompt = '''
(N)ew User Login
(E)xisting User Login
(D)elete a User
(P)rint User info
(L)ogin
(Q)uit
Enter choice: '''

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'nedplq':
                print 'invalid option, try again'
            else:
                chosen = True
            if choice == 'q': done = True
            if choice == 'n': newuser()
            if choice == 'd': delete_user()
            if choice == 'p': Print_user_info()
            if choice == 'e': olduser()
            if choice == 'l': login()

if __name__ == '__main__':
    showmenu()
