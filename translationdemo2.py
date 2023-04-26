import requests 
from bs4 import BeautifulSoup
import pandas as pd  
 
url = "https://remotive.io/" 
response = requests.get(url) 
soup = BeautifulSoup(response.text, "html.parser") 
 
jobs_wrapper = soup.find(id="initial_job_list") 
job = jobs_wrapper.find(class_="job-tile") 
job_title = job.find(class_="job-tile-title") 
print(job_title.text) 

def extract_data(job): 
	job_title = job.find(class_="job-tile-title") 
	extra = job.find("p").text.split("·") 
	return { 
		"id": job.parent.get("id"), 
		"title": job_title.text.strip(), 
		"link": job_title.get("href"), 
		"company": extra[0].strip(), 
		"location": extra[1].strip(), 
		"category": job.find(class_="remotive-tag-transparent").text, 
	} 
 
jobs_wrapper = soup.find(id="initial_job_list") 
jobs = jobs_wrapper.find_all(class_="job-tile") 
results = [extract_data(job) for job in jobs] 


data = pd.DataFrame(results) 
data.to_csv("offers.csv", index=False)

 
print(results) 