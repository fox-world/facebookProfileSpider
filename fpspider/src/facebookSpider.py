#-*-coding:utf-8-*-
'''
Created on 2014-9-7

@author: Administrator
'''
import getpass
import time
import codecs
import csv

from selenium import webdriver

from facebookLogin import FacebookLogin

import settings as S
from spider.seleniumparse import SeleniumParse
from item.fbprofileitem import FacebookProfileItem
from url import urls1 as spiderurl


class FacebookSpider(object):
    '''
    classdocs
    '''

    def inputCredential(self):
        email=raw_input('Facebook account email:')
        password=getpass.getpass()
        return {'email':email,'password':password}
    
    def parseURL(self,userinfo):
        isFirst=True
        driver=webdriver.Firefox()
        sparse=SeleniumParse()
        fbProfileItems=[]
        
        if isFirst:
            driver.get(S.URL_TO_START_PRASE)
            sparse.parseSource(sparse.loginFacebook(driver, userinfo),True)
        else:
            pass
        for u in spiderurl.URLs:
            driver.get(u[0])
            fbProfileItem=FacebookProfileItem()
            time.sleep(S.PAGE_TIME_INTERVAL)
            fbProfileItem=sparse.parseSource(driver,False)
            print u[0]
            if fbProfileItem:
                setattr(fbProfileItem,'profile_url',u[0])
                fbProfileItems.append(fbProfileItem)
        driver.close()
        self.writeCSV(fbProfileItems)
        
    def writeCSV(self,fbProfileItems):
        with open('fbprofile.csv','wb') as fcsv:
            fcsv.write(codecs.BOM_UTF8)
            writer=csv.writer(fcsv)
            writer.writerow(S.properties)
            for fb in fbProfileItems:
                fbProfileItem=[]
                for prop in S.properties:
                    fbProfileItem.append(getattr(fb,str(prop)))
                writer.writerow(fbProfileItem)
        print '*************Finished write csv file!**************'

if __name__ == '__main__':
    fbSpider=FacebookSpider()
    userinfo=fbSpider.inputCredential()
    login=FacebookLogin()
    loginFailed=not login.loginFacebook(userinfo)
    if loginFailed:
        print 'Login Facebook failed!'
    else:   
        print '--------Spider Start----------'
        startTime=time.time()   
        fbSpider.parseURL(userinfo)
        endTime=time.time()
        print '--------Spider End----------'
        print 'Total time cost:\t',(endTime-startTime)       