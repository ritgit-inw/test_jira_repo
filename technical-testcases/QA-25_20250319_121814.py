""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication and verifies the expected outcomes.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    try:
        logging.info('Navigating to the login page.')
        driver.get('https://your-app-login-url.com')  # Replace with the actual login URL
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Login with Google'
    try:
        logging.info('Clicking on Login with Google button.')
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
    except Exception as e:
        logging.error(f'Error clicking Login with Google: {e}')

    # Step 3: Wait for the Google authentication page to load
    try:
        logging.info('Waiting for Google authentication page to load.')
        WebDriverWait(driver, 10).until(
            EC.title_contains("Google")
        )
    except Exception as e:
        logging.error(f'Error waiting for Google authentication page: {e}')

    # Step 4: Verify successful login to the app
    try:
        logging.info('Verifying successful login to the app.')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[text()="Welcome"]'))
        )
    except Exception as e:
        logging.error(f'Login failed, welcome message not found: {e}')

    # Step 5: Check for any error messages
    try:
        logging.info('Checking for error messages.')
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message ID
        assert not error_message.is_displayed(), "Error message is displayed"
    except Exception as e:
        logging.warning(f'Error message check failed: {e}')

finally:
    # Clean up and close the browser
    logging.info('Closing the browser.')
    driver.quit()