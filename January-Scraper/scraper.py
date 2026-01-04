
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. SCRAPE: Get the data from the web
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# 2. EXTRACT: Pick out specific pieces
job_elements = results.find_all("div", class_="card-content")
data = []

for job in job_elements:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    data.append([title, company, location])

# 3. CLEAN: Put it in a table and remove whitespace
df = pd.DataFrame(data, columns=['Job Title', 'Company', 'Location'])
df['Location'] = df['Location'].str.replace('\n', '') # Simple cleaning

# 4. SAVE: Create first dataset
df.to_csv("january_job_data.csv", index=False)
print("Project Complete: Data saved to january_job_data.csv")
