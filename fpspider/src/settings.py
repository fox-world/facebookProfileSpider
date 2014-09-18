#-*-coding:utf-8-*-
'''
Created on 2014-9-15

@author: Administrator
'''
#second
PAGE_TIME_INTERVAL=2

MAX_WORK_INFO_SIZE=10

MAX_EDU_INFO_SIZE=10

#Before parse the urls,we need a url to make the page login,so this url is just used for login
#URL_TO_START_PRASE='https://www.facebook.com/profile.php?id=100000197722200&sk=info'
URL_TO_START_PRASE='https://www.facebook.com/profile.php?id=100000197722201&sk=info'

properties=[
            'profile_url','profile_image_url','first_name','last_name',
            
            'professional_skill','current_city','hometown','birth_date','birth_year','language','gender','phone','email','screen_name','website',
            
            'company1','position1','location1','start_date1','end_date1','description1',
            'company2','position2','location2','start_date2','end_date2','description2',
            'company3','position3','location3','start_date3','end_date3','description3',
            'company4','position4','location4','start_date4','end_date4','description4',
            'company5','position5','location5','start_date5','end_date5','description5',
            'company6','position6','location6','start_date6','end_date6','description6',
            'company7','position7','location7','start_date7','end_date7','description7',
            'company8','position8','location8','start_date8','end_date8','description8',
            'company9','position9','location9','start_date9','end_date9','description9',
            'company10','position10','location1','start_date10','end_date10','description10',
            
            'school1','graduating_year1','degree1','major1','slocation1','sdescription1',
            'school2','graduating_year2','degree2','major2','slocation2','sdescription2',
            'school3','graduating_year3','degree3','major3','slocation3','sdescription3',
            'school4','graduating_year4','degree4','major4','slocation4','sdescription4',
            'school5','graduating_year5','degree5','major5','slocation5','sdescription5',
            'school6','graduating_year6','degree6','major6','slocation6','sdescription6',
            'school7','graduating_year7','degree7','major7','slocation7','sdescription7',
            'school8','graduating_year8','degree8','major8','slocation8','sdescription8',
            'school9','graduating_year9','degree9','major9','slocation9','sdescription9',
            'school10','graduating_year10','degree10','major10','slocation10','sdescription10'
            ]
    