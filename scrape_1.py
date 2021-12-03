from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text,'lxml')
job = soup.find('li',class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3',class_ = 'joblist-comp-name').text
lst = list(map(str,company_name.split()))
if(lst[-2]+lst[-1] == '(MoreJobs)'):
    company_name = ' '.join(lst[:len(lst)-2])
else:
    company_name = ' '.join(lst)
print(company_name)
