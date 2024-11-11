from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

def driver():
    driver = webdriver.Firefox()
    #CHANGE THE DATA RANGE HERE TO WHATEVER YEAR AND MONTHS YOU WANT TO PARSE THROUGH
    start_date = datetime(1999, 1, 1)
    end_date = datetime(1999, 12, 31)
    current_date = start_date

    
    while current_date <= end_date:
         
        date_str = current_date.strftime('%m/%d/%Y')

        driver.get("https://registration.elections.myflorida.com/en/CheckVoterStatus")

        
        name = driver.find_element(By.ID, "FirstName")
        name.click()
        name.clear()   
        #WRITE THE FIRST NAME OF THE PERSON YOU WANT TO FIND HERE:
        name.send_keys('')

        last_name = driver.find_element(By.ID, "txtLastName")
        last_name.click()
        last_name.clear()
        #LAST NAME OF THE PERSON HERE: 
        last_name.send_keys("")

         
        date_field = driver.find_element(By.ID, "datepicker")
        date_field.click()
        date_field.clear()
        date_field.send_keys(date_str)

         
        check = driver.find_element(By.ID, "Acknowledged")
        check.click()

        submit = driver.find_element(By.NAME, "submitaction")
        submit.click()

        try:
            none_found = driver.find_element(By.ID, "inner-message")
            if none_found:
                print(f"None for: {date_str}")
        except:
            print(f"Record found for date: {date_str}")
           
        time.sleep(1)

         
        current_date += timedelta(days=1)

     
    driver.close()

 
driver()
