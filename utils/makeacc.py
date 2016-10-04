#!/usr/bin/python

import random, md5


def adduserandpass(user,password):
    info = ""
    if not user in users(): #check if pass is same
        info+= user.lower()+ ", " + encrypt(password) + "\n"
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

def writetofile(user,password):
    x = open("logininfo.csv","a")
    x.write(adduserandpass(user,password))
    x.close()
    
