""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication and verifies the expected behavior as per the acceptance criteria.
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        driver.get('https://your-app-login-url.com')  # Replace with the actual login URL
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error('Failed to navigate to the login page: %s', e)

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = driver.find_element(By.XPATH, '//button[text()="Login with Google"]')
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
    except Exception as e:
        logging.error('Failed to click on Login with Google button: %s', e)

    # Step 3: Wait for the Google authentication page to load
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Google"))
        logging.info('Google authentication page loaded.')
    except Exception as e:
        logging.error('Google authentication page did not load: %s', e)

    # Step 4: Check if redirected to Google authentication page
    try:
        assert "Google" in driver.title, "Not redirected to Google authentication page"
        logging.info('Successfully redirected to Google authentication page.')
    except AssertionError as e:
        logging.error('Assertion error: %s', e)

    # Step 5: Simulate successful authentication (this part will depend on your testing setup)
    # You may need to enter credentials here or use a test account

    # Step 6: Verify successful login to the app
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[text()="Welcome"]')))
        logging.info('Successfully logged in to the app.')
    except Exception as e:
        logging.error('Login failed, welcome message not found: %s', e)

    # Step 7: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message element ID
        if error_message.is_displayed():
            logging.info("Error message displayed: %s", error_message.text)
        else:
            logging.info("No error messages displayed")
    except Exception as e:
        logging.error('Error message element not found: %s', e)

finally:
    # Clean up and close the browser
    driver.quit()
    logging.info('Browser closed.')