""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: Python 3.12, Selenium, Chrome
Notes: Ensure that the ChromeDriver version matches the installed Chrome version. Adjust the sleep times as necessary based on network speed and response times.
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

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    logging.info('Navigating to the login page.')
    driver.get('https://your-app-login-url.com')  # Replace with the actual login URL

    # Step 2: Click on 'Login with Google'
    try:
        logging.info('Clicking on the Login with Google button.')
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
    except Exception as e:
        logging.error('Error clicking Login with Google button: %s', e)

    # Step 3: Wait for the Google authentication page to load
    logging.info('Waiting for the Google authentication page to load.')
    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )

    # Step 4: Check if redirected to Google authentication page
    try:
        assert "Google" in driver.title, "Not redirected to Google authentication page"
        logging.info('Successfully redirected to Google authentication page.')
    except AssertionError as e:
        logging.error(e)

    # Step 5: Simulate successful authentication (this part may vary based on your app's flow)
    # You may need to enter credentials here or handle Google login via automation

    # Step 6: Verify successful login
    try:
        logging.info('Waiting for the app to process the login.')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[text()="Welcome"]'))
        )
        assert "Welcome" in driver.page_source, "User not logged in successfully"
        logging.info('User logged in successfully.')
    except AssertionError as e:
        logging.error(e)

    # Step 7: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message ID
        assert not error_message.is_displayed(), "Error message displayed: " + error_message.text
        logging.info('No error messages displayed.')
    except Exception as e:
        logging.info('No error message element found or not displayed: %s', e)

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()