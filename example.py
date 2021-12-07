'''
REGEX LINK
CODE BY MINZ TEAM
EXAMPLE CODE BY ZEROCOOL
'''

import re

#Email Regex
re.compile(r"[^@]+@[^@]+\.[^@]+")

#Url Regex
re.compile(r'^(?:http|ftp)s?://' r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' r'localhost|' r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' r'(?::\d+)?' r'(?:/?|[/?]\S+)$', re.IGNORECASE)

#MidUser Regex
re.compile(r'u\w{32}')

#GroupId Regex
re.compile(r'c\w{32}')

#RoomId Regex
re.compile(r'r\w{32}')

#AllID Regex
re.compile(r'(?:u\w{32}|c\w{32}|r\w{32})')

##====Example Execute Code
def InstagramRegexLink(text):
    Link_instaP   = re.compile(r'^(?:http|ftp)s?://' r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' r'localhost|' r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' r'(?::\d+)?' r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    instaP = Link_instaP.findall(text)
    detect = []
    for l in instaP:
        if l not in detect:
            detect.append(l)
        else:pass
    if detect != []:
        for a in detect:
            print(str(a))

def MidUser(text):
    MID_REGEX = re.compile(r'u\w{32}')
    Mids = MID_REGEX.findall(text)
    detect = []
    for l in Mids:
        if l not in detect:
            detect.append(l)
        else:pass
    if detect != []:
        for a in detect:
            print(str(a)
