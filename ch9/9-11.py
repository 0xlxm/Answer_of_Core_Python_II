#! /usr/bin/env python

'''
9-11. Web site Addresses.
a.
    Write a URL bookmark manager. Create a text-driven menu-based application
    that allows the user to add, update, or delete entries. Entries include a site
    name, Web site URL address, and perhaps a one-line description (optional).
    Allow search functionality so that a search "word" looks through both names
    and URLs for possible matches. Store the data to a disk file when the user
    quits the application, and load up the data when the user restarts.
b.
    (b) Upgrade your solution to part (a) by providing output of the bookmarks to
    a legible and syntactically correct HTML file (.htm or .html) so that users can
    then point their browsers to this output file and be presented with a list of their
    bookmarks. Another feature to implement is allowing the creation of "folders"
    to allow grouping of related bookmarks. Extra credit: Read the literature on
    regular expressions and the Python re module. Add regular expression
    validation of URLs that users enter into their databases.
'''

import os
import re

# 8 Regular Expressions You Should Know
'''
/^[a-z0-9_-]{3,16}$/ # username
/^[a-z0-9_-]{3,16}$/ # password
/^#?([a-f0-9]{6}|[a-f0-9]{3})$/ #Hex value
/^[a-z0-9-]+$/          # slug
/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/ # email address
/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/ # url
/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/ # ip
/^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$/ # Html tag
'''

def newurl():
    db = {}
    url_pa = re.compile(r'https?://www\..*\.com')
    name = raw_input('enter a bookmark name: ')
    db['name'] = name
    url = raw_input('enter the URL: ')
    urlinfo = url_pa.findall(url)
    if urlinfo == []:
        print 'wrong url'
        return
    else:
        db['url'] = urlinfo[0]
    des = raw_input('enter the discription: ')
    db['des'] = des
    
    #return name + ',' + url + ',' + des + '\n'
    return db

def showmenu():
    bookmark = []
    prompt = '''
(N)ew URL 
(D)elete a URL
(P)rint BookMark
(Q)uit
Enter choice: '''

    html_tag_head = '''
<html>
    <head><title> My Bookmark </title></head>
    <body>
'''
    html_tag_tail = '''
    </body>
</html>
'''
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
            if choice == 'q':
                done = True
                f = open(os.path.expanduser('~/bookmark.html'), 'w')
                f.write(html_tag_head)
                for i, line in enumerate(bookmark):
                    line = '<li><a href="'+line['url']+'">'+line['name']+'</a>'+'-'+line['des']+'-\n'
                    f.write(line)
                f.write(html_tag_tail)
                f.close()
            if choice == 'n': 
                re = newurl()
                if re is not None: 
                    bookmark.append(re)
                    print bookmark
            if choice == 'd': deleteurl()

if __name__ == '__main__':
    showmenu()
