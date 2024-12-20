from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Set up the WebDriver with Service class
service = Service(ChromeDriverManager().install())  # Automatically manages chromedriver version
driver = webdriver.Chrome(service=service)

try:
    # Step 2: Open the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)  # Optional: Wait for the page to load fully

    # Step 3: Locate the username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Step 4: Enter sample credentials (valid test credentials)
    username_field.send_keys("student")
    password_field.send_keys("Password123")

    # Step 5: Click the login button
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()
    time.sleep(15)  # Optional: Wait for the login process

    # Step 6: Verify login success by checking for a specific element
    success_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Logged In Successfully')]")
    if success_message:
        print("Login successful!")
    else:
        print("Login failed.")
        
finally:
    # Close the browser after the test
    driver.quit()
