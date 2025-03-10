""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, including requesting a reset link, receiving the email, and resetting the password.
Assignee: Prakhar Soni
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the password reset page
    try:
        logging.info('Navigating to the password reset page.')
        driver.get('https://yourapp.com/password-reset')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Request a password reset link
    try:
        logging.info('Requesting a password reset link.')
        email_input = driver.find_element('name', 'email')
        email_input.send_keys('user@example.com')
        request_button = driver.find_element('id', 'request-reset')
        request_button.click()
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')

    # Wait for the email to be sent
    time.sleep(5)  # Adjust as necessary for your application

    # Step 3: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 4: Simulate receiving the email and clicking the reset link
    try:
        logging.info('Simulating receiving the email and clicking the reset link.')
        driver.get('https://yourapp.com/reset-password?token=valid_token')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')

    # Step 5: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = driver.find_element('name', 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element('name', 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element('id', 'reset-password')
        reset_button.click()
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Wait for the password to be reset
    time.sleep(5)  # Adjust as necessary for your application

    # Step 6: Check for login success
    try:
        logging.info('Checking for login success message.')
        login_message = driver.find_element('id', 'login-success')
        assert login_message.is_displayed(), 'Login success message not displayed'
    except Exception as e:
        logging.error(f'Error checking login success message: {e}')

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()