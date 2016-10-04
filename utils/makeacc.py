#!/usr/bin/python

import random, hashlib

def updatedict(user):
    users = {}
    x = open("data/logininfo.csv")
    text = x.readlines()
    x.close()
    for line in text:
        words = line.split(' ')
        username = words[0].strip(",")
        hashpass = words[1]
        users[username] = hashpass
    return users[user]
        

def adduserandpass(user,password):
    info = ""
    if not user in users():
        info+= user.lower()+ ", " + encrypt(password) + "\n"
    return info

def encrypt(password):
    return hashlib.sha256(password).hexdigest()

def users():
    ans = []
    x = open("data/logininfo.csv")
    text = x.read()
    x.close()
    info = text.split()
    for word in info:
        if "," in word:
            ans.append(word.strip(","))
    return ans

def writetofile(user,password):
    x = open("data/logininfo.csv","a")
    x.write(adduserandpass(user,password))
    x.close()
    
