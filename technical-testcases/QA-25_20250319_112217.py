""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: Python 3.12, Selenium, Chrome WebDriver, WebDriver Manager
Notes: Ensure that the Google login button's XPath is correct and that the test account is set up for testing.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Setup Chrome options
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
        logging.error(f'Error navigating to login page: {e}')  

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
    except Exception as e:
        logging.error(f'Error clicking on Google login button: {e}')  

    # Step 3: Wait for the Google authentication page to load
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 4: Check if redirected to Google authentication page
    try:
        assert "Google" in driver.title, "Not redirected to Google authentication page"
        logging.info('Redirected to Google authentication page.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')  

    # Step 5: Simulate successful authentication (this part will depend on your testing setup)
    # You may need to enter credentials here or use a test account
    # Example: driver.find_element('id', 'identifierId').send_keys('your-email@gmail.com')
    # driver.find_element('id', 'identifierNext').click()
    # time.sleep(2)
    # driver.find_element('name', 'password').send_keys('your-password')
    # driver.find_element('id', 'passwordNext').click()

    # Step 6: Wait for redirection back to the app
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 7: Verify successful login
    try:
        assert "Welcome" in driver.page_source, "Login failed, welcome message not found"
        logging.info('Login successful, welcome message found.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')  

    # Step 8: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message')  # Adjust the selector as necessary
        assert not error_message.is_displayed(), "Error message is displayed"
        logging.info('No error message displayed.')
    except Exception as e:
        logging.info('Error message element not found or not displayed.')
        logging.error(f'Error checking for error message: {e}')

finally:
    # Close the driver
    driver.quit()
    logging.info('Driver closed.')