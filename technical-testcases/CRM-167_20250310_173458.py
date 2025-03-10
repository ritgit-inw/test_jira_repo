""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, verifying each step of the process from requesting a reset to confirming the new password.
Assignee: Vikesh Bk
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

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the password reset page
    try:
        driver.get('https://yourapp.com/password-reset')
        logging.info('Navigated to the password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Request a password reset
    try:
        email_input = driver.find_element('id', 'email')
        email_input.send_keys('user@example.com')
        request_button = driver.find_element('id', 'request-reset')
        request_button.click()
        logging.info('Requested password reset for user@example.com.')
    except Exception as e:
        logging.error(f'Error requesting password reset: {e}')

    # Step 3: Verify email sent message
    try:
        time.sleep(2)  # Wait for the message to appear
        email_sent_message = driver.find_element('id', 'email-sent-message')
        assert email_sent_message.is_displayed(), 'Email sent message is not displayed'
        logging.info('Email sent message is displayed.')
    except Exception as e:
        logging.error(f'Error verifying email sent message: {e}')

    # Step 4: Simulate clicking the link in the email
    try:
        driver.get('https://yourapp.com/reset-password?token=valid_token')
        logging.info('Navigated to the reset password link.')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')

    # Step 5: Set a new password
    try:
        new_password_input = driver.find_element('id', 'new-password')
        new_password_input.send_keys('NewStrongPassword123!')
        confirm_password_input = driver.find_element('id', 'confirm-password')
        confirm_password_input.send_keys('NewStrongPassword123!')
        reset_button = driver.find_element('id', 'reset-password')
        reset_button.click()
        logging.info('New password set and reset button clicked.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Step 6: Verify confirmation message
    try:
        time.sleep(2)  # Wait for the message to appear
        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message is not displayed'
        logging.info('Confirmation message is displayed.')
    except Exception as e:
        logging.error(f'Error verifying confirmation message: {e}')

finally:
    driver.quit()
    logging.info('WebDriver closed.')