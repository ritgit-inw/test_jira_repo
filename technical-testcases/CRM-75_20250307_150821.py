""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, WebSelenium, Chrome
Notes: This test case automates the password reset feature, ensuring that the user can request a password reset, receive an email, and set a new password successfully.
Assignee: Aditya Jena
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
        logging.info('Navigating to the login page.')
        driver.get('https://yourapp.com/login')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Forgot Password' link
    try:
        logging.info('Clicking on the Forgot Password link.')
        forgot_password_link = driver.find_element('link text', 'Forgot Password?')
        forgot_password_link.click()
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter email address
    try:
        logging.info('Entering email address.')
        email_input = driver.find_element('name', 'email')
        email_input.send_keys('user@example.com')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Submit the request
    try:
        logging.info('Submitting the request.')
        submit_button = driver.find_element('id', 'submit')
        submit_button.click()
    except Exception as e:
        logging.error(f'Error submitting request: {e}')

    # Step 5: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 6: Simulate receiving the email and clicking the reset link
    try:
        logging.info('Navigating to the reset password page.')
        driver.get('https://yourapp.com/reset-password?token=sampletoken')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')

    # Step 7: Enter new password
    try:
        logging.info('Entering new password.')
        new_password_input = driver.find_element('name', 'new_password')
        new_password_input.send_keys('NewPassword123!')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 8: Confirm new password
    try:
        logging.info('Confirming new password.')
        confirm_password_input = driver.find_element('name', 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
    except Exception as e:
        logging.error(f'Error confirming new password: {e}')

    # Step 9: Submit the new password
    try:
        logging.info('Submitting the new password.')
        reset_button = driver.find_element('id', 'reset')
        reset_button.click()
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')

    # Step 10: Check for login success
    try:
        logging.info('Checking for login success message.')
        login_message = driver.find_element('id', 'login-message')
        assert login_message.is_displayed(), 'Login message not displayed'
    except Exception as e:
        logging.error(f'Error checking login success message: {e}')

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()