from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    #print(job.text,end = '\n')
    publish_date = job.find('span',class_ = 'sim-posted').text.strip()
    if(publish_date in ['Posted today','Posted few days ago']):
        company_name = job.find('h3',class_ = 'joblist-comp-name').text
        lst = list(map(str,company_name.split()))
        if(lst[-2]+lst[-1] == '(MoreJobs)'):
            company_name = ' '.join(lst[:len(lst)-2])
        else:
            company_name = ' '.join(lst)
    #print(company_name)

        skills_str = job.find('span',class_ = 'srp-skills').text.replace(' ','').replace('\r\n','')
        skills = list(map(str,skills_str.split(',')))
        skills_str = ', '.join(skills).strip()
        #print(skills)

        more_info = job.header.h2.a['href']
        print(f"Company Name: {company_name}")
        print(f"Skills Required: {skills_str}")
        print(f"More Info: {more_info}",end = '\n\n')     


