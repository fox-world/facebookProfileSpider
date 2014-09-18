'''
Created on 2014-9-15

@author: Administrator
'''

class BasicInfoSpider(object):
    '''
    Parse person basic information
    '''

    def parse_content(self,cmt_soup,fbProfileItem):
        
        basicdiv=cmt_soup.find('div',{'id':'pagelet_basic'})
        if basicdiv:
            self.get_basic_info(basicdiv,fbProfileItem)
        
        contactdiv=cmt_soup.find('div',{'id':'pagelet_contact'})
        if contactdiv:
            self.get_contact_info(contactdiv, fbProfileItem)
    
    def get_basic_info(self,info_soup,fbProfileItem):
        basicul=info_soup.find('ul')
        if basicul.find('span',text='No basic info to show'):
            return
        for basicli in basicul:
            infotype=basicli.div.div.span.get_text().strip()
            infocontent=basicli.div.div.find_next_sibling('div').span.get_text().strip()
            self.parse_basic_info(infotype, infocontent,fbProfileItem)      
    
    def get_contact_info(self,info_soup,fbProfileItem):
        contactul=info_soup.find('ul')
        if contactul.find('span',text='No contact info to show'):
            return
        for contactli in contactul:
            infotype=contactli.div.div.span.get_text().strip()
            infocontent=contactli.div.div.find_next_sibling('div').span.get_text().strip()
            self.parse_contact_info(infotype, infocontent,fbProfileItem)      
    
    def parse_basic_info(self,infotype,infocontent,fbProfileItem):
        if infotype=='Gender':
            setattr(fbProfileItem,'gender',infocontent)
            print 'Gender:\t',infocontent
        elif infotype=='Languages':
            setattr(fbProfileItem,'language',infocontent)
            print 'Languages:\t',infocontent
        elif infotype=='Birthday':
            contents=infocontent.split(',')
            if len(contents)==2:
                setattr(fbProfileItem,'birth_date',contents[0])
                setattr(fbProfileItem,'birth_year',contents[1])
                print 'Birth Date:\t',contents[0]
                print 'Birth Year:\t',contents[1]
            else:
                setattr(fbProfileItem,'language',infocontent)
                setattr(fbProfileItem,'birth_date',infocontent)
                print 'Birth Date:\t',infocontent
                
    def parse_contact_info(self,infotype,infocontent,fbProfileItem):
        if infotype=='Website':
            setattr(fbProfileItem,'screen_name','Website')
            setattr(fbProfileItem,'website',infocontent)
            print 'Website:\t',infocontent
        elif infotype=='Facebook':
            setattr(fbProfileItem,'screen_name','Facebook')
            setattr(fbProfileItem,'website',infocontent)
            print 'Facebook:\t',infocontent
        else:
            pass

    
