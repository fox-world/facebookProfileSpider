#-*-coding:utf-8-*-
'''
Created on 2014-9-7

@author: Administrator
'''
import time
import re

from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys

import settings as S
from workeduspider import WorkEduSpider
from addressspider import AddressSpider
from basicinfospider import BasicInfoSpider
from item.fbprofileitem import FacebookProfileItem

class SeleniumParse(object):
    
    fbProfileItem=None
    
    '''
    classdocs
    '''
    def loginFacebook(self,driver,userinfo):
        elem=driver.find_element_by_id("email")
        elem.send_keys(userinfo['email'])
        elem=driver.find_element_by_id('pass')
        elem.send_keys(userinfo['password'])
        elem.send_keys(Keys.RETURN)
        time.sleep(S.PAGE_TIME_INTERVAL)
        return driver
        
    def parseSource(self,driver,isFirst):
        
        if isFirst:
            return None
        
        print '======================================='
        
        pagesource=driver.page_source
        
        if 'Page Not Found' in pagesource:
            print '++++++++Empty record+++++++++'
            return None
        else:
            self.fbProfileItem=FacebookProfileItem()
            
            cmt_soup=BeautifulSoup(pagesource)
            
            self.get_profile_image_url(cmt_soup)
            self.get_names(cmt_soup)
            self.get_tab_info(cmt_soup,driver)
            
            return self.fbProfileItem
    
    def get_tab_info(self,cmt_soup,driver):
        workedu=cmt_soup.find('span',text=re.compile("Work and Education"))
        if workedu:
            driver.get(workedu.parent['href'])
            time.sleep(S.PAGE_TIME_INTERVAL)
            self.get_work_edu(driver.page_source)
             
        places=cmt_soup.find('span',text=re.compile("Places He's Lived|Places She's Lived"))
        if places:
            driver.get(places.parent['href'])
            time.sleep(S.PAGE_TIME_INTERVAL)
            self.get_live_info(driver.page_source)
        
        contacts=cmt_soup.find('span',text=re.compile("Contact and Basic Info"))
        if contacts:
            driver.get(contacts.parent['href'])
            time.sleep(S.PAGE_TIME_INTERVAL)
            self.get_basi_info(driver.page_source)
             
#         details=cmt_soup.find('span',text=re.compile('Details About \w+'))
#         if details:
#             print 'Details info:\t',details.parent['href']
        
    def get_profile_image_url(self,cmt_soup):
        image_url=cmt_soup.find('img',class_='profilePic img',src=True)
        if image_url:
            profile_image_url=image_url['src']
            self.fbProfileItem.profile_image_url=profile_image_url
            print 'Profile image url:\t',profile_image_url  
            
    def get_names(self,cmt_soup):
        title=cmt_soup.title
        if title:
            title=title.get_text()
            names=title.split()
            first_name=names[0]
            last_name=' '.join(names[1:])
            self.fbProfileItem.first_name=first_name
            self.fbProfileItem.last_name=last_name
            print 'First name:\t',first_name.encode('utf-8')
            print 'Last name:\t',' ',last_name
            
    def get_work_edu(self,pagesource):
        cmt_soup=BeautifulSoup(pagesource)
        workeduspider=WorkEduSpider()
        workeduspider.parse_content(cmt_soup,self.fbProfileItem)
        
    def get_live_info(self,pagesource):
        cmt_soup=BeautifulSoup(pagesource)
        addressspider=AddressSpider()
        addressspider.parse_content(cmt_soup,self.fbProfileItem)
        
    def get_basi_info(self,pagesource):
        cmt_soup=BeautifulSoup(pagesource)
        basicinfospider=BasicInfoSpider()
        basicinfospider.parse_content(cmt_soup,self.fbProfileItem)