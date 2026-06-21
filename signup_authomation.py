from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://authorized-partner.vercel.app/")

# STEP 1: Fill first page fields (example structure)
wait.until(EC.presence_of_element_located((By.XPATH, "//input")))

driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("testuser123@mail.com")
driver.find_element(By.NAME, "password").send_keys("Test@123")

driver.save_screenshot("screenshots/page1.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

# STEP 2: Second page (example structure)
wait.until(EC.presence_of_element_located((By.XPATH, "//input")))

driver.find_element(By.NAME, "phone").send_keys("9800000000")

driver.save_screenshot("screenshots/page2.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

# STEP 3: Final submit
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))

driver.save_screenshot("screenshots/before_submit.png")

driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

driver.save_screenshot("screenshots/success.png")

print("Signup automation completed")

time.sleep(3)
driver.quit()
