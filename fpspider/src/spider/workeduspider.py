#-*-coding:utf-8-*-
'''
Created on 2014-9-14

@author: Administrator
'''

import re

import settings as S

class WorkEduSpider(object):
    '''
    Parse information for work and education
    '''
    
    def parse_content(self,cmt_soup,fbProfileItem):
        
        skillspan=cmt_soup.find('span',text=u'Professional Skills')
        if skillspan:
            skills=skillspan.parent.find_next_sibling('ul')
            skillstr=None
            for skill in skills.find_all('a'):
                if skillstr is None:
                    skillstr=skill.get_text()
                else:
                    skillstr=skillstr+' , '+skill.get_text()
            if skillstr:
                setattr(fbProfileItem,'professional_skill',skillstr)
                print 'Skill:\t',skillstr
        
        #parse work information
        workspan=cmt_soup.find('span',text='Work')
        if workspan:
            works=workspan.parent.find_next('ul')
            worder=0
            for work in works.find_all('li'):
                worder=worder+1
                if worder>S.MAX_WORK_INFO_SIZE:
                    break;
                company=work.find('a',{'data-hovercard':not None})
                workinfo=work.find('div',class_="fsm fwn fcg")
                if company:
                    comp=company.get_text().strip()
                    setattr(fbProfileItem,'company'+str(worder),comp)
                    print 'Company name',worder,':\t',comp
                if workinfo:
                    self.parse_work(workinfo.get_text(),worder,fbProfileItem)
        
        #parse education information
        eduspan=cmt_soup.find('span',text=u'Education')
        if eduspan:
            edus=eduspan.parent.find_next('ul')
            eorder=0
            for edu in edus.find_all('li'):
                school=edu.find('a',{'data-hovercard':not None})
                schoolinfo=edu.find('div',class_="fsm fwn fcg")
                if school:
                    #exclude the classmates information
                    classmates1=school.find_next_sibling('img',{'data-hover':'tooltip'})
                    classmates2=school.find_next_sibling('a',{'role':'button'})
                    if not classmates1 and not classmates2:
                        eorder=eorder+1
                        if eorder>S.MAX_EDU_INFO_SIZE:
                            break;
                        sch=school.get_text().strip()
                        setattr(fbProfileItem,'school'+str(eorder),sch)
                        print 'School',eorder,':\t',sch
                        if schoolinfo:
                            self.parse_edu_info(schoolinfo.get_text().strip(), eorder,fbProfileItem)
             
    
    def parse_work(self,work_soup,order,fbProfileItem):
        works=work_soup.split('·')
        workslen=len(works)
        if workslen==1:
            if re.compile('\d{4}').search(works[0].strip()):
                self.get_work_start_end_time(works[0].strip(),order,fbProfileItem)
            else:
                position=works[0].strip()
                setattr(fbProfileItem,'position'+str(order),position)
                print 'Position',order,':\t',position
        elif workslen==2:
            position=works[0].strip()
            setattr(fbProfileItem,'position'+str(order),position)
            print 'Position',order,':\t',position
            if re.compile('\d{4}').search(works[1]):
                self.get_work_start_end_time(works[1],order,fbProfileItem)
            else:
                setattr(fbProfileItem,'location'+str(order),works[1])
                print 'Location',order,':\t',works[1]
        elif workslen==3:
            position=works[0].strip()
            setattr(fbProfileItem,'position'+str(order),position)
            print 'Position',order,':\t',position
            self.get_work_start_end_time(works[1],order,fbProfileItem)
            location=works[2]
            setattr(fbProfileItem,'location'+str(order),location)
            print 'Location',order,':\t',location
        else:
            position=works[0].strip()
            setattr(fbProfileItem,'position'+str(order),position)
            print 'Position',order,':\t',position
                
    def get_work_start_end_time(self,work_time,order,fbProfileItem):
        if 'to ' in work_time:
            work_times=work_time.split('to ')
            start_time=work_times[0]
            end_time=work_times[1]
            setattr(fbProfileItem,'start_date'+str(order),start_time)
            setattr(fbProfileItem,'end_date'+str(order),end_time)
            print 'Start time',order,':\t',start_time
            print 'End time',order,':\t',end_time
        else:
            setattr(fbProfileItem,'start_date'+str(order),work_time)
            print 'Start time',order,':\t',work_time
                
    
    def parse_edu_info(self,edu_soup,order,fbProfileItem):
        
        containyear=False
            
        edus=edu_soup.split('·')
        eduslen=len(edus)
        if eduslen>1:
            pattern=re.compile('\d{4}')#using regex to check if the sentence contains the graduation year
            if pattern.search(edu_soup):
                containyear=True
        
        slocation=edus[-1]
        setattr(fbProfileItem,'slocation'+str(order),slocation)        
        print 'Location',order,':\t',slocation
        
        if eduslen==1:
            pass
        elif eduslen==2:
            if containyear:
                self.get_edu_graduating_year(edus[0], order,fbProfileItem)
            else:
                setattr(fbProfileItem,'major'+str(order),edus[0])
                print 'Major',order,':\t',edus[0]
        elif eduslen==3:
            if containyear:
                self.get_edu_graduating_year(edus[0], order,fbProfileItem)
                setattr(fbProfileItem,'major'+str(order),edus[1])
                print 'Major',order,':\t',edus[1]
            else:
                setattr(fbProfileItem,'major'+str(order),edus[-2])
                print 'Major',order,':\t',' '.join(edus[:-2])
        else:
            if containyear:
                self.get_edu_graduating_year(edus[0], order,fbProfileItem)
                setattr(fbProfileItem,'major'+str(order),edus[1])
                print 'Major',order,':\t',edus[1]
            else:
                setattr(fbProfileItem,'major'+str(order),edus[1:-1])
                print 'Major',order,':\t',' '.join(edus[1:-1])
    
    def get_edu_graduating_year(self,edu_soup,order,fbProfileItem):
        if 'to ' in edu_soup:
            edu_years=edu_soup.split('to ')
            setattr(fbProfileItem,'graduating_year'+str(order),edu_years[1])
            print 'Graduating year',order,':\t',edu_years[1]
        else:
            setattr(fbProfileItem,'graduating_year'+str(order),edu_soup)
            print 'Graduating year',order,':\t',edu_soup
           

        