'''
Created on 2014-9-7

@author: Administrator
'''
import urllib2 
import cookielib

class FacebookLogin(object):
    '''
    Login facebook using python
    '''


    def __init__(self):
        '''
        Constructor
        '''
        cookie=cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
                            ('Content-Type', 'application/x-www-form-urlencoded'),
                            ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]
        self.opener=opener
        
    def loginFacebook(self,userinfo):
            
        url = 'https://login.facebook.com/login.php?login_attempt=1'
        data = "locale=en_US&non_com_login=&email="+userinfo['email']+"&pass="+userinfo['password']+"&lsd=20TOl"

        self.opener.open('http://www.facebook.com')
        usock = self.opener.open(url, data)
    
        if "Logout" in usock.read():
            return True
        else:
            return False