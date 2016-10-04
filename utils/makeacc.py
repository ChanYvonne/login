#!/usr/bin/python

import random, cgitb, cgi, md5, csv
cgitb.enable()

def adduserandpass():
    form = cgi.FieldStorage()
    keys = form.keys()
    info = ""
    if 'user' in keys and "pass" in keys:
         if not form['user'].value in users() and form['user'].value.isalnum():
                info+= form['user'].value.lower()+ ", " + encrypt(form['pass'].value) + "\n"
    return info

def encrypt(password):
    m = md5.new()
    m.update(password)
    hashpass=m.hexdigest()
    return hashpass

def users():
    ans = []
    x = open("logininfo.csv")
    text = x.read()
    x.close()
    info = text.split()
    for word in info:
        if "," in word:
            ans.append(word.strip(","))
    return ans

def writetofile():
    form = cgi.FieldStorage()
    keys = form.keys()
    x = open("logininfo.csv","a")
    x.write(adduserandpass())
    x.close()
    
