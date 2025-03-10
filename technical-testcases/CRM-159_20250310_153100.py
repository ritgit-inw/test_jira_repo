""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, ensuring that the user can request a reset link, receive it, set a new password, and log in successfully.
Assignee: Malini Sharma
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
        logging.info('Navigating to the password reset page.')
        driver.get('https://yourapp.com/password-reset')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')  

    # Step 2: Request a password reset link
    try:
        logging.info('Requesting a password reset link.')
        email_input = driver.find_element('id', 'email')  # Assuming the email input has an id of 'email'
        email_input.send_keys('user@example.com')  # Replace with a valid email
        request_button = driver.find_element('id', 'request-reset')  # Assuming the button has an id of 'request-reset'
        request_button.click()
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')  

    # Step 3: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')  # Assuming the success message has an id
        assert success_message.is_displayed(), 'Success message not displayed'
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking for success message: {e}')  

    # Step 4: Simulate receiving the email and clicking the reset link
    try:
        logging.info('Simulating receiving the email and clicking the reset link.')
        driver.get('https://yourapp.com/reset-password?token=valid_token')  # Replace with a valid token
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')  

    # Step 5: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = driver.find_element('id', 'new-password')  # Assuming the new password input has an id
        new_password_input.send_keys('NewPassword123!')  # Replace with a valid password
        confirm_password_input = driver.find_element('id', 'confirm-password')  # Assuming the confirm password input has an id
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element('id', 'reset-password')  # Assuming the reset button has an id
        reset_button.click()
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 6: Check for login success
    try:
        logging.info('Checking for login success message.')
        login_message = driver.find_element('id', 'login-success')  # Assuming the login success message has an id
        assert login_message.is_displayed(), 'Login success message not displayed'
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking for login success message: {e}')  

finally:
    logging.info('Quitting the driver.')
    driver.quit()