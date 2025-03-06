""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case verifies the password reset functionality by simulating a user entering their email and checking for success/error messages.
Assignee: Vikesh Bk
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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
    # Navigate to the password reset page
    logging.info('Navigating to the password reset page.')
    driver.get('https://your-application-url.com/password-reset')

    try:
        # Enter email address
        logging.info('Entering email address.')
        email_input = driver.find_element('name', 'email')
        email_input.send_keys('user@example.com')
        logging.info('Email address entered successfully.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    try:
        # Click on the reset password button
        logging.info('Clicking on the reset password button.')
        reset_button = driver.find_element('id', 'reset-password')
        reset_button.click()
        logging.info('Reset password button clicked successfully.')
    except Exception as e:
        logging.error(f'Error clicking reset password button: {e}')

    try:
        # Check for success message
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    try:
        # Check for error message if email is not registered
        logging.info('Checking for error message.')
        error_message = driver.find_element('id', 'error-message')
        assert not error_message.is_displayed(), 'Error message should not be displayed'
        logging.info('No error message displayed as expected.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking error message: {e}')

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()