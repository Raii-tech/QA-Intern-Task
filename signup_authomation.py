from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Open Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://the-internet.herokuapp.com/upload")

# Get absolute file path
file_path = os.path.abspath("test-data/company_registration.pdf")

# Upload file
upload_box = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
upload_box.send_keys(file_path)

print("File selected successfully!")

# Click Upload button
driver.find_element(By.ID, "file-submit").click()

time.sleep(2)

print("File uploaded successfully!")

driver.quit()