""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, ensuring that the user can request a reset link, receive it, and successfully reset their password.
Assignee: Aswin Suresh
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
    # Step 1: Navigate to the password reset page
    try:
        driver.get('https://yourapp.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Request a password reset link
    try:
        email_input = driver.find_element('name', 'email')
        email_input.send_keys('user@example.com')
        request_button = driver.find_element('id', 'request-reset')
        request_button.click()
        logging.info('Requested password reset link.')
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')

    # Step 3: Check for success message
    try:
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Simulate receiving the email and clicking the reset link
    try:
        driver.get('https://yourapp.com/reset-password?token=valid_token')
        logging.info('Navigated to reset password link.')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')

    # Step 4: Set a new password
    try:
        new_password_input = driver.find_element('name', 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element('name', 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element('id', 'reset-password')
        reset_button.click()
        logging.info('New password set.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Step 5: Check for login success
    try:
        login_message = driver.find_element('id', 'login-success')
        assert login_message.is_displayed(), 'Login success message not displayed'
        logging.info('Login success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking login success message: {e}')

finally:
    driver.quit()