""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication. Ensure to replace placeholders with actual values.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('https://your-app-login-url.com')  # Replace with the actual login URL
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error('Failed to navigate to the login page: %s', e)

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
    except Exception as e:
        logging.error('Failed to click on Login with Google button: %s', e)

    # Step 3: Wait for Google authentication page to load
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 4: Perform Google login
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
        )
        email_input.send_keys(os.getenv('GOOGLE_EMAIL'))  # Use environment variable
        email_input.submit()
        logging.info('Entered email and submitted.')
    except Exception as e:
        logging.error('Failed to enter email: %s', e)

    time.sleep(2)  # Wait for the next page to load

    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
        )
        password_input.send_keys(os.getenv('GOOGLE_PASSWORD'))  # Use environment variable
        password_input.submit()
        logging.info('Entered password and submitted.')
    except Exception as e:
        logging.error('Failed to enter password: %s', e)

    # Step 5: Verify successful login
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Welcome")]'))
        )
        logging.info('Login successful, welcome message displayed.')
    except Exception as e:
        logging.error('Login failed or welcome message not displayed: %s', e)

    # Step 6: Check for error messages if login fails
    try:
        error_message = driver.find_element(By.XPATH, '//div[@class="error-message"]')  # Adjust the XPath as necessary
        if error_message.is_displayed():
            logging.error('Error message displayed: %s', error_message.text)
        else:
            logging.info('No error message displayed.')
    except Exception as e:
        logging.info('No error message element found or not displayed: %s', e)

finally:
    # Close the driver
    driver.quit()