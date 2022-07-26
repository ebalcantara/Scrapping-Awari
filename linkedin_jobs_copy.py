## All Imports
from driverutils import ChromeBot
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support import ui
from time import sleep

## Parameters
URL_LINKEDIN = 'https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br'

# XPATHS
DESCRIPTION = 'show-more-less-html__markup'
JOB_CRITERIA='description__job-criteria-item'
JOB_TITLE = 'top-card-layout__title'
COMPANY = 'topcard__org-name-link'
LOCATION = 'topcard__flavor--bullet'
JOB_RESULTS_BAR = 'base-card__full-link'

## Classes and Functions

## Execution

# Scrap with Selenium
c = ChromeBot()
c.driver.implicitly_wait(5)
c.driver.get(URL_LINKEDIN)
wait = ui.WebDriverWait(c, 120)

all_description = []
all_locations = []
all_titles = []
all_company = []
all_criterias = []

len_results = 0
print(len_results)
all_results = c.driver.find_elements(By.CLASS_NAME, JOB_RESULTS_BAR)
print(len(all_results))
while len(all_results)>len_results:
    for r in all_results[len_results:]:        
        sleep(1.8)
        r.click()
        wait
        description = c.driver.find_element(By.CLASS_NAME, DESCRIPTION).text
        if description == "":
            r.click()
            sleep(2)
        print(description)
        location = c.driver.find_element(By.CLASS_NAME, LOCATION).text
        company = c.driver.find_element(By.CLASS_NAME, COMPANY).text
        title = c.driver.find_element(By.CLASS_NAME, JOB_TITLE).text
        criteria = c.driver.find_element(By.CLASS_NAME, JOB_CRITERIA).text
        c.driver.execute_script("arguments[0].scrollIntoView();", r)

        all_description.append(description)
        all_locations.append(location)
        all_titles.append(title)
        all_company.append(company)
        all_criterias.append(criteria)

	#print(all_locations)
	#print(all_company)
	#print(all_titles)

    len_results = len(all_results)
    all_results = c.driver.find_elements(By.CLASS_NAME, JOB_RESULTS_BAR)
    print(len_results)
    print(len(all_results))

# Export to CSV
export_data = {'company':all_company, 'title':all_titles, 'location': all_locations, 'criteria':all_criterias, 'description':all_description}
df = pd.DataFrame(export_data)
print(df.head())
df.to_excel("linkedin_data_science_jobs.xlsx", index = False)
